# 🎵 Spotify Popularity Predictor (Machine Learning API)

Este proyecto implementa un modelo de Machine Learning (Random Forest) capaz de predecir la popularidad de una canción en Spotify basándose en sus características técnicas y el perfil del artista.

El sistema está compuesto por un pipeline completo de Ciencia de Datos, una API REST construida con FastAPI y una interfaz gráfica interactiva desarrollada en Streamlit.

# Equipo de Desarrollo

- Lautaro Daniel Short
- Fernando Agustín Laprida
- Leandro Francisco Franco Sian

# Stack Tecnológico

- **Data Science & Modelado:** Python, Pandas, Scikit-Learn, Joblib
- **Backend (API REST):** FastAPI, Uvicorn, Pydantic
- **Frontend (Interfaz Gráfica):** Streamlit, Requests

Instrucciones de Ejecución (Local

**Instalar las dependencias:**

uv pip install -r requirements.txt

*Levantar el Servidor Backend (FastAPI):
uvicorn servidor:app --reload
*Levantar la Interfaz Gráfica (Streamlit)(En una nueva terminal):
streamlit run app.py
\*Acceder al link proporcionado en la terminal de app.py

# ¿Qué modelo se usó y por qué?

Usamos un **Random Forest** (bosque aleatorio) con 100 árboles de decisión.  
Cada árbol aprende a predecir la popularidad haciendo preguntas simples (por ejemplo, "¿la popularidad del artista es mayor a 50?"). Al final, se promedian las respuestas de todos los árboles para obtener una predicción más estable.

Existen muchos otros modelos (regresión lineal, Gradient Boosting, redes neuronales...), pero elegimos Random Forest porque:

- Es fácil de entender y de explicar.
- Captura relaciones no lineales (la popularidad no sube siempre en línea recta).
- Funciona bien sin necesidad de ajustar mucho los datos.
- Nos dice qué variables influyen más, ayudándonos a interpretar los resultados.
- Con pocos datos y variables es un excelente punto de partida.

# Resultados obtenidos

- **R² Score:** 0.37 (explica el 37 % de la variación en la popularidad).
- **Error promedio (RMSE):** 16.4 puntos de popularidad.

Esto significa que, en promedio, el modelo se equivoca por unas 16 posiciones en el ranking de popularidad.

# ¿Por qué el modelo no es más preciso?

La popularidad de una canción depende mucho de **cómo suena** (ritmo, energía, etc.) y de factores externos (listas de reproducción, marketing).  
Como nuestro dataset **no tiene esas características acústicas**, el modelo no puede capturar la mayor parte de la información que determina si una canción será popular o no.  
En otras palabras: **el límite no está en el algoritmo, sino en los datos disponibles**. Con mediciones acústicas, el mismo modelo podría funcionar mucho mejor.

# Conclusión

Este proyecto demuestra que, para predecir popularidad musical, es esencial contar con datos sobre el sonido de las canciones. Sin ellos, incluso el mejor modelo solo puede llegar hasta cierto punto.
