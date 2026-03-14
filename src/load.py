import pandas as pd
from sqlalchemy import create_engine, text
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import types

load_dotenv()

def obtener_conexion():
  
    password = os.getenv('PASSWORD_DB')
    username = os.getenv('USER_DB')
    server = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    
    driver = "ODBC+Driver+18+for+SQL+Server" 
    
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}&TrustServerCertificate=yes"
    engine = create_engine(connection_string)
    
    return engine


def upsert_table(df, table_name, pk_columns, engine):
  
    if isinstance(pk_columns, str):
        pk_columns = [pk_columns]

    stg_table = f"stg_{table_name}"

    dtype_mapping = {}
    for col_name in df.select_dtypes(include=['datetime', 'datetimetz']).columns:
        dtype_mapping[col_name] = types.DateTime() 

    df.to_sql(stg_table, con=engine, if_exists='replace', index=False, dtype=dtype_mapping)
    

    columns = df.columns.tolist()
    
    update_columns = [col for col in columns if col not in pk_columns]
    
    on_conditions = " AND ".join([f"TARGET.{col} = SOURCE.{col}" for col in pk_columns])
    
    update_set = ", ".join([f"TARGET.{col} = SOURCE.{col}" for col in update_columns])
    insert_cols = ", ".join(columns)
    insert_vals = ", ".join([f"SOURCE.{col}" for col in columns])
    
    if update_columns:
        update_clause = f"WHEN MATCHED THEN UPDATE SET {update_set}"
    else:
        update_clause = "" 

    merge_query = f"""
    MERGE {table_name} AS TARGET
    USING {stg_table} AS SOURCE
    ON {on_conditions}
    
    {update_clause}
        
    WHEN NOT MATCHED BY TARGET THEN
        INSERT ({insert_cols})
        VALUES ({insert_vals});
    """
    
    
    with engine.begin() as conn:
        conn.execute(text(merge_query))
        conn.execute(text(f"DROP TABLE {stg_table}"))



def proceso_load(df_productos, df_usuarios, df_ventas):
    print("Iniciando proceso de carga Incremental (UPSERT)...")
    engine = obtener_conexion()
    
    try:
        print(" Haciendo Upsert de dim_productos")
        upsert_table(df_productos, 'dim_productos', 'product_id', engine)
        
        print(" Haciendo Upsert de dim_usuarios")
        upsert_table(df_usuarios, 'dim_usuarios', 'user_id', engine) 
        
        print(" Haciendo Upsert de fact_ventas...")
        upsert_table(df_ventas, 'fact_ventas', ['id_venta', 'product_id'], engine)
        
    except Exception as e:
        print(f" Error crítico durante la carga a la base de datos: {e}")
        raise e