# API de Predicción de Ingresos

Este repositorio contiene una API REST desarrollada con FastAPI para la predicción de ingresos basada en un modelo de Machine Learning.

## Descripción

La API expone dos endpoints principales:

*   `/`:  Endpoint raíz que devuelve un mensaje de bienvenida.
*   `/predict`: Endpoint para realizar predicciones de ingresos.  Este endpoint está protegido por autenticación mediante clave API.

## Arquitectura

La API se construye utilizando las siguientes tecnologías:

*   **FastAPI:** Framework web moderno y de alto rendimiento para construir APIs con Python.
*   **Uvicorn:** Servidor ASGI para ejecutar la API.
*   **joblib:** Librería para cargar el modelo de Machine Learning previamente entrenado.
*   **pandas:** Librería para manipulación y análisis de datos.

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git](https://www.google.com/search?q=https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git)  # Reemplaza con tu URL
    cd NOMBRE_DEL_REPOSITORIO
    ```

2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt  # Asegúrate de tener un archivo requirements.txt con las dependencias
    ```

## Uso

1.  **Configuración de la clave API:**

    *   **Desarrollo:** Crea un archivo `.env` en el mismo directorio que `docker-compose.yml` con la variable `ingresos` y tu clave API:

        ```
        ingresos=TU_CLAVE_API_AQUI
        ```

2.  **Ejecutar la API con Docker Compose (Recomendado):**

    ```bash
    docker-compose up -d --build
    ```

3.  **Interactuar con la API:**

    *   **Endpoint raíz:**

        ```bash
        curl http://localhost:8000/
        ```

    *   **Endpoint de predicción (`/predict`):**

        *   **Método:** `POST`
        *   **Encabezado:** `X-API-Key: TU_CLAVE_API_AQUI`
        *   **Cuerpo (JSON):**  Datos de entrada para el modelo.  Deben coincidir con las columnas de entrenamiento del modelo.

            ```json
            {
              "feature1": valor1,
              "feature2": valor2,
              // ... otros features
            }
            ```

        *   **Ejemplo (usando `curl`):**

            ```bash
            curl -X POST -H "X-API-Key: TU_CLAVE_API_AQUI" -H "Content-Type: application/json" -d '{ "feature1": valor1, "feature2": valor2, ... }' http://localhost:8000/predict
            ```

    *   **Generar clave API**

        ```bash
        curl http://localhost:8000/generate_api_key
        ```

        Este endpoint genera una clave API aleatoria para pruebas. 

## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`: