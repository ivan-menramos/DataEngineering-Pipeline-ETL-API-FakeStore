import sys
from src.Extract import extraer_productos, extraer_usuarios, extraer_carts
from src.Transform import transformacion_productos, transformacion_usuarios, transformacion_carts
from src.load import proceso_load


def main():

    try:
        datos_productos = extraer_productos()
        datos_usuarios = extraer_usuarios()
        datos_carts = extraer_carts()
        print("Extracción de la API completada")

        df_productos = transformacion_productos(datos_productos)
        df_usuarios = transformacion_usuarios(datos_usuarios)
        df_ventas = transformacion_carts(datos_carts)
        print("Limpieza y transformación completada.")

        print("\n[3/3] --- Fase de Carga ---")
        proceso_load(df_productos, df_usuarios, df_ventas)
        print("Carga en SQL Server completada.")

    except Exception as e:
        print(f"\nHa ocurrido un error crítico en el flujo ETL: {e}")
        sys.exit(1) 

if __name__ == "__main__":
    main()