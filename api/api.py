# api.py
import os
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
import uvicorn
import joblib
import pandas as pd
import secrets  # Para generar claves API seguras (solo para desarrollo)

app = FastAPI()

# --- Autenticación con Clave API ---
API_KEY_NAME = "X-API-Key"  # Nombre del encabezado para la clave API
api_key_header = APIKeyHeader(name=API_KEY_NAME)

# Obtener la clave API desde una variable de entorno (¡para producción!)
API_KEY = os.environ.get("ingresos")  # Usa el nombre correcto de tu variable
if API_KEY is None:
    raise ValueError("La variable de entorno ingresos no está definida.") # Mensaje de error más descriptivo

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="No autorizado")
    return api_key

# --- Cargar Modelo ---
try:
    pipeline = joblib.load("../resultados/pipeline_total.gz")
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Modelo no encontrado.")

@app.get("/")
def read_root():
    return {"message": "API para predicción de ingresos"}

@app.post("/predict", dependencies=[Depends(verify_api_key)])  # Protege el endpoint /predict
async def predict(data: dict):
    try:
        input_df = pd.DataFrame([data])
        columnas_entrenamiento = pipeline.named_steps['preprocesador'].transformers_[0][2].tolist() + pipeline.named_steps['preprocesador'].transformers_[1][2].tolist()
        input_df = input_df[columnas_entrenamiento]
        prediction = pipeline.predict(input_df)
        prediction_proba = pipeline.predict_proba(input_df)
        return {"prediction": int(prediction[0]), "probability": prediction_proba[0][1]}
    except ValueError as ve:  # Ejemplo de manejo específico de excepciones
        raise HTTPException(status_code=400, detail=f"Error de validación de entrada: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

# --- Generar Clave API (para pruebas - ¡ELIMINAR EN PRODUCCIÓN!) ---
@app.get("/generate_api_key")  # ¡ELIMINAR EN PRODUCCIÓN!
def generate_api_key():
    new_key = secrets.token_urlsafe(32)  # Genera una clave aleatoria fuerte
    return {"api_key": new_key}  # En una app real, almacena esto de forma segura y devuélvelo al usuario

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)