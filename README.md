# Predicción de Ingresos - Construcción y Publicación de APP y APIs

![GitHub repo size](https://img.shields.io/github/repo-size/Michel221212/prediccion-ingresos-hym)
![GitHub contributors](https://img.shields.io/github/contributors/Michel221212/prediccion-ingresos-hym)
![GitHub stars](https://img.shields.io/github/stars/Michel221212/prediccion-ingresos-hym?style=social)

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI 0.68.1](https://img.shields.io/badge/fastapi-0.68.1-blue.svg)
![uvicorn 0.15.0](https://img.shields.io/badge/uvicorn-0.15.0-blue.svg)
![Streamlit 1.30.0](https://img.shields.io/badge/streamlit-1.30.0-red.svg)

![GitHub forks](https://img.shields.io/github/forks/Michel221212/prediccion-ingresos-hym?style=social)
**Ejercicio de APIs**

# Actividad presentada por

### - Hannan Nayibe Yousef Novoa
### - Yohn Forthis Hernandez Mendoza
### - Michel Stivens Larrota Villalba

# Actividad: Ajuste código de Machine Learning

El presente repositorio tiene como propósito presentar un producto para la materia de Gerencia de Proyectos para Ciencia de Datos, el cual se representa en el ajuste del código suministrado en la clase realizada el 15 de febrero de 2025 en las instalaciones de la Universidad EAN, para la generación del resultado final se presenta el siguiente registro de fases y actividades:

## Fases y actividades desarrolladas

Este proyecto se enfoca en desarrollar un modelo de machine learning para la predicción de ingresos, junto con una API y una aplicación para su despliegue y uso.

### Fase 1: Organización del Proyecto y Creación de Ramas
1. Crea el repositorio en GitHub.
2. Crear las tres ramas (modelo, api, app).
3. Cargar los archivos suministrados, de acuerdo a las especificaciones del proyecto.
4. Estandarizar la estructura de los archivos.
5. Crear el archivo README.md en cada rama explicando su alcance.

### Fase 2: Ajuste del Código para la Parametrización de los Datos
1. Revisión y ajuste del código de carga de datos y análisis descriptivo.
2. Revisión y ajuste del código de limpieza y parametrización de datos.
3. Revisión y ajuste del código de entrenamiento del modelo.
4. Revisión y ajuste del código de generación del Pipeline.
4. Prueba de todas las funcionalidades.

### Fase 3: Ajuste y Parametrización de API y APP
1. Revisión y ajuste del código para la API.
2. Revisión y ajuste del código para la APP.
3. Prueba de todas las funcionalidades.

### Fase 4: Dockerización del Proyecto
1. Crear Dockerfile en cada rama (modelo/, api/, app/)
2. Escribir un docker-compose.yml que orqueste los servicios
3. Probar que todo funcione corriendo docker-compose up

### Fase 5: Integración Final
1. Pruebas de integración: modelo → API → App

#### Carga de la API y la APP 
<div style="text-align: left;">
<image src="resultados/carga-api-app.png" alt="Carga en sistema de la API y la APP" width="600" height="265">
</div>

#### Carga del formulario y la predicción

<div style="text-align: left;">
<image src="resultados/carga-formulario.png" alt="Carga del formulario de registro y predicción" width="600" height="1002">
</div>

#### Carga completa del ambiente en Docker Desktop

<div style="text-align: left;">
<image src="resultados/docker-desktop.png" alt="Evidencia de carga completa en el Docker Desktop" width="600" height="691">
</div>

## Estructura del proyecto

```.
ingresos_ml/
├── api/
│   ├── api.py                  # Código de la API
│   ├── Dockerfile              # Dockerfile para la API
│   └── README.md               # Proporciona información general de la rama api
│   ├── requirements.txt        # Lista de dependencias generales de la rama api
├── app/
│   ├── app.py                  # Código de la aplicación Streamlit
│   ├── Dockerfile              # Dockerfile para la aplicación Streamlit
│   └── README.md               # Proporciona información general de la rama app
│   ├── requirements.txt        # Lista de dependencias generales de la rama app
├── modelo/
│   ├── Dockerfile              # Dockerfile para el modelo
│   ├── README.md               # Proporciona información general de la rama modelo     
│   ├── requirements.txt        # Lista de dependencias generales de la rama modelo
│   └── train.py                # Este archivo (código de parametrización de los datos y entrenamiento)
├── resultados/                 
│   ├── carga-api-app.png       # Pantallazo que evidencia la carga en sistema de la API y la APP
│   ├── carga-formulario.png    # Pantallazo que evidencia la carga en sistema del formulario y la predicción
│   ├── docker-desktop.png      # Pantallazo que evidencia la carga en sistema del ambiente en Docker Desktop
│   ├── mejor_modelo.gz         # Modelo de Machine Learning entrenado y optimizado
│   ├── pipeline_total.gz       # Pipeline completo de preprocesamiento y transformación de datos
│   └── preprocesador.gz        # Objeto o conjunto de instrucciones para el preprocesamiento de datos
├── .env                        # Archivo de configuración para variables de entorno
├── docker-compose.yml          # Archivo de configuración de Docker Compose
├── poetry.lock                 # Archivos de configuración y dependencias para Poetry
├── pyproject.toml              # Archivos de configuración y dependencias para Poetry
├── README.md                   # proporciona información general del proyecto
└── requirements.txt            # Lista de dependencias generales del proyecto
```

## Descripción de los componentes

* **`api/`**: Contiene el código de la API desarrollada con Python (`api.py`), junto con un Dockerfile para su contenedorización.
* **`app/`**: Incluye el código de la aplicación (posiblemente web) que interactúa con la API (`app.py`), también con su propio Dockerfile.
* **`modelo/`**: Alberga los scripts y archivos relacionados con el modelo de machine learning:
    * `train.py`: Script para el entrenamiento del modelo.
    * `requirements.txt`: Lista de dependencias necesarias para el modelo.
    * Archivos del modelo pre-entrenado (`.gz`).
* **`resultados/`**: Almacena imágenes y archivos resultantes del entrenamiento y despliegue, como gráficos y modelos serializados.
* **Archivos raíz:**
    * `.env`: Archivo de configuración para variables de entorno.
    * `docker-compose.yml`: Archivo para la gestión de contenedores con Docker Compose.
    * `poetry.lock` y `pyproject.toml`: Archivos de configuración y dependencias para Poetry.
    * `README.md`: Este archivo, que proporciona información general del proyecto.
    * `requirements.txt`: Lista de dependencias generales del proyecto.

## Investigación de Concepto - Docker

### Definición

Es una herramienta de software que permite crear, implementar y administrar aplicaciones en contenedores. Contenedor, definido como una unidad de software que contiene todo lo necesario para ejecutar una aplicación, incluidos los archivos, los binarios, las bibliotecas y los entornos de ejecución, es así como se puede “Dockerizar” aplicaciones de Python, Angular, React, dodnet o inclusive bases de datos y por supuesto aplicaciones enfocadas a la Ciencia de Datos.

### Terminologías básicas

#### Docker Compose
Es una herramienta que permite definir y administrar grupos de contenedores relacionados entre si. Es un archivo de texto de composición de Docker que define los contenedores que se van a crear, sus dependencias, volúmenes, registros y redes que usaran.

#### Dockerfile
Es un simple archivo de texto que define cómo crear una imagen de contenedor, consta de una serie de instrucciones que se ejecutan de forma secuencial, por ejemplo, como los archivos .sh de linux.

#### Docker Hub
Registro público para cargar imágenes y trabajar con ellas. En este gran repositorio de imágenes es donde podremos encontrar imágenes de aplicaciones, de software y de sistemas que usaremos para crear nuestros contenedores. Puedes crear una cuenta y subir tus propias imágenes y tenerlas públicas o privadas.

#### Docker Engine
Es el componente central de Docker que permite crear, implementar y administrar todos los contenedores.

#### Docker Daemon
Proceso que se ejecuta en segundo plano y controla los contenedores. En Linux se llama docker.service.

### Instalación

#### API de Docker
La API de Docker es una interfaz de programación de aplicaciones que se puede utilizar para controlar los contenedores de forma automatizada, con ella se puede crear y desplegar sistemas un poco más fácil desde el punto de vista del programador siempre y cuando el proyecto requiera mantenimientos futuros.

Ahora que sabemos que es y para que sirve, pasemos al tema principal, como puedo instalarlo y sobre todo como usarlo para la ciencias de datos.

#### Cómo instalar Docker
Para este ejemplo, se explica como instalar Docker en Linux Debian:

Se actualiza el sistema operativo:
```bash
sudo apt update
```
Se realiza la configuración necesaria e instala los paquetes requeridos, se ejecutan los siguientes códigos línea por línea:
```bash
sudo apt install apt-transport-https lsb-release ca-certificates curl gnupg -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io
```
Se inicia el servicio Docker:
```bash
sudo systemctl start docker
```
luego se habilita el servicio para que se inicie automáticamente al arrancar Linux:
```bash
sudo systemctl enable docker
```
### Aplicación

#### Docker con la ciencia de datos
Docker se puede utilizar para ciencia de datos de varias maneras. Una forma es utilizar Docker para crear entornos de desarrollo reproducibles. Esto permite a los científicos e ingenieros de datos compartir sus proyectos o ejecutarlos en cualquier entorno.

Otra forma es utilizar Docker para crear aplicaciones de ciencia de datos que se puedan implementar en producción. Esto permite crear aplicaciones que se puedan ejecutar en cualquier entorno, sin tener que preocuparse por las dependencias o la configuración, luego los científicos de datos pueden usar esas mismas aplicaciones para entornos de aprendizajes automatizados para que luego los analistas de datos puedan entregar visualizaciones de gráficos para la toma de decisiones.

#### Casos de usos

##### Caso de uso 1: Desarrollo de modelos de aprendizaje automático
Un científico de datos podría crear un Dockerfile que defina un entorno que incluya Python, TensorFlow y todas las dependencias necesarias para desarrollar un modelo de aprendizaje automático. Este Dockerfile podría compartirse con otros científicos de datos para que puedan comenzar a desarrollar sus propios modelos de aprendizaje automático sin tener que instalar Python, TensorFlow o ninguna de las dependencias anteriores.

#####  Caso de uso 2: Implementación de aplicaciones de aprendizaje automático
Se crea un Dockerfile nuevamente, este documento de texto va a definir lo necesario para crear una aplicación de aprendizaje automático que se utilice para clasificar imágenes. Este Dockerfile podría implementarse en un servidor para que la aplicación esté disponible para todos los usuarios. Luego de su uso se puede ejecutar en distintos entornos y trabajar su automatización.

#####  Caso de uso 3: Analítica de datos en tiempo real
Crear varios contenedores, el primero con un código ETL (Extract, Transform, Load) en Python que extraiga data de un sitio web las 24 horas del día cada minuto, luego tener otro contenedor con Apache Kafka que sirva como canalización de datos y un tercer contenedor con Apache Druid la cual es una Base de Datos NoSQL, donde se almacena dicha información. Para poder conectar esa base de datos y crear gráficos se podría usar Apache Superset, el cual es un potente creador de gráficas para la toma de decisiones y que tiene el poder de conectar varias bases de datos.

Referencia: Tejada, J. C. R. (2020, septiembre 28). Docker para la ciencia de datos. Medium. https://jcrtejada05.medium.com/docker-para-la-ciencia-de-datos-c584c83f0eaf
