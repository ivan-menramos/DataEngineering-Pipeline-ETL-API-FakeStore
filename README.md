
##  Descripción del Proyecto
Este proyecto es un pipeline **ETL (Extract, Transform, Load)** automatizado y contenedorizado, diseñado para procesar datos de comercio electrónico. Extrae información cruda desde una API RESTful externa, limpia y transforma los datos utilizando Python (Pandas), y los carga en una base de datos **SQL Server** modelada y normalizada para garantizar la integridad referencial.

Como **Matemático Aplicado**, mi enfoque en este proyecto no fue solamente mover los datos, sino diseñar una **arquitectura de datos robusta** aplicando los principios de normalización  y preparándola para su consumo analítico.

##  Arquitectura del Sistema


1. **Extracción:** Se consume la `FakeStore API` utilizando la librería `requests` de Python, extrayendo entidades como Productos, Usuarios y Carritos de compra en formato JSON.
2. **Transformación:** Los datos en memoria son procesados con `pandas`. Se manejan valores nulos, se corrigen tipos de datos y se estructuran para encajar en el modelo relacional.
3. **Carga:** Se utiliza SQLAlchemy para insertar los datos limpios en **SQL Server**.
4. **Infraestructura:** Todo el entorno está orquestado mediante **Docker Compose**, lo que garantiza que el pipeline sea reproducible en cualquier sistema sin conflictos de dependencias.

##  Modelado de Datos
Para soportar futuras consultas analíticas y mantener la consistencia, la base de datos fue diseñada aplicando normalización:
* **Dim_Products:** Contiene información descriptiva de los artículos y categorías.
* **Dim_Users:** Almacena la información demográfica de los clientes.
* **Fact_Sales:** Tabla transaccional que registra las compras, conectando productos y usuarios.

##  Tecnologías Utilizadas
* **Lenguaje:** Python (Pandas, Requests, SQLAlchemy)
* **Base de Datos:** Microsoft SQL Server 
* **DevOps & Infraestructura:** Docker, Docker Compose
* **Orquestación:** Apache Airflow 

## Resultados
* A continuación se muestra el esquema relacional de la base de datos aplicando un modelado en estrella
![Esquema relacional](<img width="1179" height="856" alt="EsquemaEstrella" src="https://github.com/user-attachments/assets/dec0ec33-42e2-4277-ab4e-2b14ed94aafe" />
)
