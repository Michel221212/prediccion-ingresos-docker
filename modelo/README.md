# Entrenamiento del Modelo de Predicción de Ingresos

Este script de Python (`train.py`) se encarga de entrenar un modelo de Machine Learning para predecir si los ingresos de una persona superan los 50K al año, basándose en datos demográficos y laborales.

## Descripción

El script realiza las siguientes tareas:

1.  **Carga de datos:**  Descarga el conjunto de datos "Adult" del repositorio UCI Machine Learning.
2.  **Preprocesamiento de datos:**
    *   Elimina duplicados.
    *   Codifica la variable objetivo (`Income`) como 0 (<=50K) y 1 (>50K).
    *   Realiza imputación de valores faltantes.
    *   Aplica One-Hot Encoding a las variables categóricas.
    *   Escala las variables numéricas.
3.  **Entrenamiento del modelo:**
    *   Divide los datos en conjuntos de entrenamiento y prueba.
    *   Utiliza un modelo RandomForestClassifier.
    *   Realiza una búsqueda de hiperparámetros utilizando GridSearchCV con validación cruzada estratificada.
4.  **Evaluación del modelo:**
    *   Evalúa el modelo con el conjunto de prueba.
    *   Calcula la precisión (accuracy), el informe de clasificación y la matriz de confusión.
5.  **Guardado del modelo:**
    *   Guarda el mejor modelo entrenado.
    *   Crea y guarda un pipeline que incluye el preprocesamiento y el modelo.

## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`:

## Ejecución

1.  **Asegúrate de tener las dependencias instaladas:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Ejecuta el script:**

    ```bash
    python train.py
    ```

## Resultados

El script guardará los siguientes archivos en la carpeta `resultados`:

*   `mejor_modelo.gz`:  El mejor modelo entrenado.
*   `pipeline_total.gz`:  Pipeline que incluye el preprocesamiento y el modelo.
*   `preprocesador.gz`:  Transformador de columnas para el preprocesamiento.

## Notas

*   El conjunto de datos "Adult" se descarga automáticamente del repositorio UCI Machine Learning.
*   El script utiliza un modelo RandomForestClassifier, pero se puede modificar para utilizar otros modelos.
*   La búsqueda de hiperparámetros se realiza con GridSearchCV, pero se pueden utilizar otras técnicas de optimización.
*   El script guarda el mejor modelo y el pipeline para que puedan ser utilizados posteriormente para realizar predicciones.
