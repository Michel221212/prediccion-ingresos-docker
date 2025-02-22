# api.py
from fastapi import FastAPI, HTTPException
import uvicorn
import joblib
import pandas as pd

app = FastAPI()

# --- Cargar Modelo ---
try:
    pipeline = joblib.load("../resultados/pipeline_total.gz")
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Modelo no encontrado.")

@app.get("/")
def read_root():
    return {"message": "API para predicción de ingresos"}

@app.post("/predict")
async def predict(data: dict):
    try:
        input_df = pd.DataFrame([data])
        columnas_entrenamiento = pipeline.named_steps['preprocesador'].transformers_[0][2].tolist() + pipeline.named_steps['preprocesador'].transformers_[1][2].tolist()
        input_df = input_df[columnas_entrenamiento]
        prediction = pipeline.predict(input_df)
        prediction_proba = pipeline.predict_proba(input_df)
        return {"prediction": int(prediction[0]), "probability": prediction_proba[0][1]}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Error de validación de entrada: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)