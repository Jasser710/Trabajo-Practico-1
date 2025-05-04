# 🎬 Trabajo Práctico 1 - Predicción de Ratings de Películas con XGBoost

Este repositorio contiene el Trabajo Práctico 1 para la materia de MLOps. El objetivo del proyecto es construir un modelo de regresión utilizando **XGBoost** para predecir el rating de películas en función de diversas características (año, audiencia y género).

## 📁 Contenido del repositorio

- `Trabajo_Práctico1.ipynb`: Notebook principal con todo el desarrollo del proyecto.
- `merged_dataset.csv`: Dataset utilizado.
- `imdb_xgboost_model.pkl`: Modelo entrenado y guardado.
- `requirements.txt`: Dependencias necesarias.
- `.gitignore`: Archivos y carpetas excluidas del control de versiones.
- `README.md`: Este archivo.

## ⚙️ Requisitos

- Python 3.8 o superior
- pip
- Entorno virtual (recomendado)

## 🚀 Instrucciones para correr el proyecto

### 1. Clonar el repositorio

git clone https://github.com/Jasser710/Trabajo-Practico-1.git  
cd Trabajo-Practico-1

### 2. Crear y activar un entorno virtual

python -m venv venv

# Activar:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

### 3. Instalar las dependencias

pip install -r requirements.txt

### 4. (Opcional) Registrar el entorno para Jupyter Notebook

pip install notebook ipykernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"

### 5. Ejecutar el notebook

jupyter notebook

Seleccionar el archivo `Trabajo_Práctico1.ipynb` y correr las celdas.

## 📊 Resultado del modelo

- Métrica: RMSE y R² score
- Modelo: XGBoost Regressor con GridSearchCV

El modelo entrenado se guarda como `imdb_xgboost_model.pkl`.

## ✍️ Autor

- Nombre: Jasser Palacios
- GitHub: [https://github.com/Jasser710](https://github.com/Jasser710)

## 📌 Notas

Este proyecto fue desarrollado con fines educativos. Para reproducir los resultados correctamente, se recomienda ejecutar todo dentro de un entorno virtual.

