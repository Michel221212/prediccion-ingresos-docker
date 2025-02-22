# Aplicación de Predicción de Ingresos

Esta aplicación web, desarrollada con Streamlit, proporciona una interfaz de usuario para interactuar con una API de predicción de ingresos.

## Descripción

La aplicación permite a los usuarios ingresar datos demográficos y laborales a través de un formulario. Al enviar el formulario, la aplicación envía una solicitud a una API (que debe estar ejecutándose por separado) para obtener una predicción sobre si los ingresos de una persona superan los 50K al año, basándose en los datos proporcionados.

## Arquitectura

La aplicación utiliza las siguientes tecnologías:

*   **Streamlit:**  Framework de Python para crear aplicaciones web interactivas de forma rápida y sencilla.
*   **Requests:**  Librería de Python para realizar solicitudes HTTP a la API.

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

    *   **Producción:** Utiliza Docker secrets o Streamlit secrets para almacenar la clave API. Consulta la documentación para más detalles.

2.  **Ejecutar la aplicación con Docker Compose (Recomendado):**

    ```bash
    docker-compose up -d --build
    ```

3.  **Acceder a la aplicación:**

    Abre un navegador web y visita la URL proporcionada por Streamlit (generalmente `http://localhost:8501`).

4.  **Utilizar la aplicación:**

    *   Completa el formulario con los datos de la persona.
    *   Haz clic en "Predecir".
    *   La aplicación mostrará la predicción de ingresos ("0" para <=50K, "1" para >50K).

## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`:
