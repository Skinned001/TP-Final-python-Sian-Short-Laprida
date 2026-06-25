from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# --- SEGURIDAD DE RUTA ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models','modelo_spotify.pkl')

app = FastAPI(title="API de Predicción de Popularidad Spotify")

# Cargamos el modelo
modelo = joblib.load(MODEL_PATH)

# Esquema de ingreso de datos
class CancionInput(BaseModel):
    track_number: int
    explicit: int
    artist_popularity: int
    artist_followers: int
    album_total_tracks: int
    album_type: int
    track_duration_min: float

@app.post("/predict")
def predict(data: CancionInput):
    # Convertimos los datos a un DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    columnas_esperadas = [
        'track_number', 
        'explicit', 
        'artist_popularity', 
        'artist_followers', 
        'album_total_tracks', 
        'album_type', 
        'track_duration_min'
    ]
    # Forzamos a que el DataFrame tenga exactamente este orden
    input_df = input_df[columnas_esperadas]
    
    # Hacemos la predicción
    prediccion = modelo.predict(input_df)[0]
    
    return {
        "popularidad_estimada": round(float(prediccion), 2),
        "mensaje": "Predicción realizada con éxito"
    }

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}