import pandas as pd

def transformacion_productos(datosP):
    
    try:
        dfP = pd.json_normalize(datosP, sep='_')

        columnas = {
            'id': 'product_id',
            'title': 'product_name',
            'price': 'product_price',
            'category': 'product_category',
            'rating_rate': 'product_rating',
            'rating_count': 'product_count'
        }
        
        dfP = dfP[list(columnas.keys())].rename(columns=columnas)
    
    except KeyError as e:
        print(f"La solicitud no regresó una de las columnas esperadas: {e}")
        raise

    num_cols = dfP.select_dtypes(include=['number']).columns
    dfP[num_cols] = dfP[num_cols].fillna(dfP[num_cols].mean().fillna(0))
    dfP = dfP.fillna('N/A')
    return dfP



def transformacion_usuarios(datosU):
    
    try:
        dfU = pd.json_normalize(datosU, sep='_')

        columnas = {
            'id': 'user_id',
            'name_firstname': 'first_name',
            'name_lastname': 'last_name',
            'username': 'username',
            'email': 'email',
            'address_city': 'city',
            'address_zipcode': 'zipcode'
        }

        dfU = dfU[list(columnas.keys())].rename(columns=columnas)
    except KeyError as e:
        print(f"La solicitud no regresó una de las columnas esperadas: {e}")
        raise

    num_cols = dfU.select_dtypes(include=['number']).columns
    dfU[num_cols] = dfU[num_cols].fillna(dfU[num_cols].mean().fillna(0))
    dfU = dfU.fillna('N/A')
    return dfU


def transformacion_carts(datosC):

    try:
        dfC = pd.json_normalize(
            datosC, 
            record_path=['products'], 
            meta=['id', 'userId', 'date'],
            errors='ignore'
        )
        
        dfC = dfC.rename(columns={
            'id': 'id_venta',
            'productId': 'product_id',
            'userId': 'user_id'
        })
        
        columnas = ['id_venta', 'product_id', 'user_id', 'date', 'quantity']
        dfC = dfC[columnas]

    except KeyError as e:
        print(f"La solicitud no regresó una de las columnas esperadas {e}")
        raise
    
    numeric_cols = dfC.select_dtypes(include=['number']).columns
    dfC[numeric_cols] = dfC[numeric_cols].fillna(dfC[numeric_cols].mean().fillna(0))
    dfC = dfC.fillna('N/A')
    dfC['date'] = pd.to_datetime(dfC['date'])
    return dfC