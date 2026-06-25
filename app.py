import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Spotify Predictor", page_icon="🎵")
st.title("🎵 Predicción de Éxitos en Spotify")
st.markdown("Ingresa las características de la canción para consultar con la Inteligencia Artificial.")

# --- FORMULARIO DE ENTRADA ---
st.header("1. Datos de la Canción")

col1, col2 = st.columns(2)

with col1:
    track_number = st.number_input("Número de Pista en el álbum", min_value=1, value=1)
    artist_popularity = st.slider("Popularidad del Artista (0-100)", 0, 100, 50)
    artist_followers = st.number_input("Seguidores del Artista", min_value=0, value=100000)
    track_duration_min = st.number_input("Duración (minutos)", min_value=0.0, value=3.5, step=0.1)

with col2:
    album_type = st.selectbox("Tipo de Lanzamiento", options=[1, 2, 3], format_func=lambda x: {1: "Álbum", 2: "Single", 3: "Compilación"}[x])
    album_total_tracks = st.number_input("Total de pistas en el lanzamiento", min_value=1, value=1)
    explicit = st.selectbox("¿Contenido Explícito?", options=[0, 1], format_func=lambda x: "Sí" if x == 1 else "No")

# --- BOTÓN DE PREDICCIÓN Y CONEXIÓN A LA API ---
if st.button("Predecir Popularidad"):
    # Armamos el diccionario exactamente igual al CancionInput de FastAPI
    datos_cancion = {
        "track_number": track_number,
        "explicit": explicit,
        "artist_popularity": artist_popularity,
        "artist_followers": artist_followers,
        "album_total_tracks": album_total_tracks,
        "album_type": album_type,
        "track_duration_min": track_duration_min
    }
    
    # Hacemos la petición POST a tu servidor FastAPI
    try:
        # st.spinner muestra una animación de carga mientras espera la respuesta
        with st.spinner('Consultando al modelo Random Forest...'):
            respuesta = requests.post("http://127.0.0.1:8000/predict", json=datos_cancion)
            
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            st.success("¡Predicción exitosa!")
            # Mostramos el resultado en grande
            st.metric(label="Popularidad Estimada", value=f"{resultado['popularidad_estimada']} / 100")
        else:
            st.error(f"Error del servidor: {respuesta.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("🚨 No se pudo conectar con el servidor backend. ¿Está FastAPI corriendo en el puerto 8000?")

st.divider()

# --- ESTADÍSTICAS DEL MODELO 
st.header("📊 Estadísticas de Rendimiento del Modelo")
st.markdown("Estas métricas corresponden al modelo *Random Forest Regressor* tras la fase de ingeniería de datos y filtrado de la 'Cola Larga' de Spotify.")

col_stat1, col_stat2 = st.columns(2)
col_stat1.metric(label="Precisión Explicada (R² Score)", value="31.8%", delta="Baseline validado")
# Usamos delta_color="inverse" porque en el RMSE, que baje el número es algo bueno
col_stat2.metric(label="Margen de Error Promedio (RMSE)", value="17.09 puntos", delta="-2.22 (Mejora por filtrado)", delta_color="inverse")