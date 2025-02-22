# api.py
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
import uvicorn
import joblib
import pandas as pd
import secrets  # Para generar claves API seguras

app = FastAPI()

# --- Autenticación con Clave API ---
API_KEY_NAME = "X-API-Key"  # Nombre del encabezado para la clave API
api_key_header = APIKeyHeader(name=API_KEY_NAME)

# Almacena las claves API de forma segura (¡reemplazar en producción!)
# En producción, considera usar un almacén de secretos como HashiCorp Vault, AWS Secrets Manager, etc.
API_KEYS = {"clave_segura_1": "usuario1", "clave_segura_2": "usuario2"}  # Diccionario para almacenar las claves API

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key not in API_KEYS:
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
    # En una app real, almacena esto de forma segura y devuélvelo al usuario
    # No olvides agregarla al diccionario API_KEYS
    return {"api_key": new_key}  # Devuelve la nueva clave API generada

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)