# Importamos la clase FastAPI desde el módulo fastapi
from fastapi import FastAPI 

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Definimos una ruta (endpoint) para el método HTTP GET, asociada al path raíz ('/')
@app.get('/')
def hello_word():
    # Cuando se accede a esta ruta, retorna un diccionario JSON con la clave "hello" y el valor "world"
    return { "hello": "world" }
