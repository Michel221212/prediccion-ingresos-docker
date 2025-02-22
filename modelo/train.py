# train.py
import pandas as pd
import numpy as np
import joblib

from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carga de datos
adult = fetch_ucirepo(id=2)
X = adult.data.features
y = adult.data.targets
df = pd.DataFrame(X, columns=adult.variables.name[:-1])
df['Income'] = y

# Preprocesamiento de datos
df=df.drop_duplicates()
df['Income'].value_counts()
(df['Income']=='>50K').value_counts()
df['Income'] = df['Income'].replace({'<=50K': 0, '>50K': 1, '<=50K.': 0, '>50K.': 1})
df['Income'].value_counts()
X = df.drop('Income', axis=1)
y = df['Income']
columnas_numericas = X.select_dtypes(exclude='object').columns
columnas_categoricas = X.select_dtypes(include='object').columns

transformacion_OHE = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
transformacion_nan = SimpleImputer(strategy='constant', fill_value='Desconocido')
transformacion_escalar = StandardScaler()

pasos = [('imputacion', transformacion_nan), ('codificacion', transformacion_OHE)]
preprocesador_categorical = ColumnTransformer(transformers=[('CAT', Pipeline(pasos), columnas_categoricas)])
preprocsador_numerico = ColumnTransformer(transformers=[('escalar', transformacion_escalar, columnas_numericas)])

Transformacion_Columnas = ColumnTransformer(
    transformers=[('num', preprocsador_numerico, columnas_numericas),
                  ('cat', preprocesador_categorical, columnas_categoricas)])

Transformacion_Columnas.fit(X)
joblib.dump(Transformacion_Columnas, 'resultados/preprocesador.gz')
new_column_transformer = joblib.load('resultados/preprocesador.gz')
columnas_numericas=Transformacion_Columnas.transformers_[0][2]
columnas_categoricas_transformadas=Transformacion_Columnas.named_transformers_['cat'].named_transformers_['CAT'][-1].get_feature_names_out()

# Entrenamiento del modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

parametros = {'n_estimators': [100, 200, 500],
              'max_depth': [5, 10, 20],
              'min_samples_split': [5, 10, 20],
              'min_samples_leaf': [1, 2, 10]}
modelo = RandomForestClassifier(random_state=42)

grid = GridSearchCV(modelo, param_grid=parametros, cv=StratifiedKFold(n_splits=5), n_jobs=-1)
grid.fit(Transformacion_Columnas.transform(X_train), y_train)

best_model = grid.best_estimator_
print('Mejores hiperparámetros:', grid.best_params_)

# Evaluación del modelo
y_pred = best_model.predict(Transformacion_Columnas.transform(X_test))
print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nClassification Report:\n', classification_report(y_test, y_pred))
print('\nConfusion Matrix:\n', confusion_matrix(y_test, y_pred))

# Guardado del mejor modelo
joblib.dump(best_model, 'resultados/mejor_modelo.gz')

# Creación y guardado del pipeline
pipeline = Pipeline(steps=[('preprocesador', Transformacion_Columnas), ('modelo', best_model)])
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, 'resultados/pipeline_total.gz')

print("Entrenamiento completado. Resultados almacenados en la carpeta 'resultados', modelo guardado como 'mejor_modelo.gz' y pipeline guardado como 'pipeline_total.gz'")