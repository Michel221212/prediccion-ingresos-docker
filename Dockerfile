# Usa una imagen base con Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala poetry
RUN pip install poetry

# Configurar Poetry para no crear un entorno virtual
RUN poetry config virtualenvs.create false

# Copia los archivos de configuración de Poetry
COPY pyproject.toml poetry.lock ./

# Instala dependencias
RUN poetry lock && poetry install --no-dev --no-interaction

# Copia el resto de la aplicación
COPY . .

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando para iniciar la aplicación Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0", "--server.port=8501"]