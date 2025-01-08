# Importamos la clase FastAPI desde el módulo fastapi
from fastapi import FastAPI 

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Definimos una ruta (endpoint) para el método HTTP GET, asociada al path raíz ('/')
@app.get('/')
def home():
    return "Hola mundo"

@app.get('/saludo')
def home():
    return "HELLO WORLD"
@app.get('/saludos')
def home():
    return "HELLO"