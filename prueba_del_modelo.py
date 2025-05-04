import joblib
import pandas as pd

# Cargar el modelo desde el archivo
loaded_model = joblib.load("imdb_xgboost_model.pkl")

# Nuevo dato (debe tener las mismas columnas que X)
nuevo_dato = pd.DataFrame([{
    'Release Year': 2020,
    'Audience': 'PG-13',
    'Film Type': 'Action'
}])

# Predecir usando el modelo cargado
prediccion = loaded_model.predict(nuevo_dato)

print(f"Predicción de IMDb Rating: {prediccion[0]}")
