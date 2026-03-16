import requests


def extraer_productos():
    """
    Falta añadir comentarios
    """
    urlP = "https://fakestoreapi.com/products"
    respuestaP = requests.get(urlP)

    if respuestaP.status_code != 200:
        print(f"Ha ocurrido un error al momento de llamar a {urlP} ")

    datosP = respuestaP.json()
    return datosP

def extraer_usuarios():
    urlU = "https://fakestoreapi.com/users"
    respuestaU = requests.get(urlU)

    if respuestaU.status_code != 200:
        print(f"Ha ocurrido un error al momento de llamar a {urlU} ")

    datosU = respuestaU.json()
    return datosU


def extraer_carts():
    urlC = "https://fakestoreapi.com/carts"
    respuestaC = requests.get(urlC)

    if respuestaC.status_code != 200:
        print(f"Ha ocurrido un error al momento de llamar a {urlC}")

    datosC = respuestaC.json()
    return datosC
