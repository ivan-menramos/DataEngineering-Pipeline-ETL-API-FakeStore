#  una imagen oficial de Python ligera
FROM python:3.11-slim-bullseye

# instalar herramientas del sistema y el Driver ODBC 18 de Microsoft para SQL Server
RUN apt-get update && apt-get install -y curl apt-transport-https gnupg2 unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# crear una carpeta dentro del contenedor donde vivirá nuestro proyecto
WORKDIR /app

# copiar e instalar los requerimientos primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar el resto del código de tu proyecto al contenedor
COPY . .

# el comando que se ejecutará al encender el contenedor
CMD ["python", "main.py"]