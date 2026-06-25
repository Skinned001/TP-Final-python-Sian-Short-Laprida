# 🎵 Spotify Popularity Predictor (Machine Learning API)

Este proyecto implementa un modelo de Machine Learning (Random Forest) capaz de predecir la popularidad de una canción en Spotify basándose en sus características técnicas y el perfil del artista. 

El sistema está compuesto por un pipeline completo de Ciencia de Datos, una API REST construida con FastAPI y una interfaz gráfica interactiva desarrollada en Streamlit.

# Equipo de Desarrollo
* Lautaro Daniel Short
* Fernando Agustín Laprida
* Leandro Francisco Franco Sian
* 
# Stack Tecnológico
* **Data Science & Modelado:** Python, Pandas, Scikit-Learn, Joblib
* **Backend (API REST):** FastAPI, Uvicorn, Pydantic
* **Frontend (Interfaz Gráfica):** Streamlit, Requests

Instrucciones de Ejecución (Local

**Instalar las dependencias:**

pip install -r requirements.txt

*Levantar el Servidor Backend (FastAPI):
uvicorn servidor:app --reload
*Levantar la Interfaz Gráfica (Streamlit)(En una nueva terminal):
streamlit run app.py
*Acceder al link proporcionado en la terminal de app.py
