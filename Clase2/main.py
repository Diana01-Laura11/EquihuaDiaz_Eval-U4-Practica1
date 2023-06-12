from fastapi import FastAPI,Query,Body

app = FastAPI()

@app.get("/peticion-1")
def peticion_1_wrapper(edad: int,estado: str, estudiante:bool):
    return {"edad":edad, "estado":estado, "estudiante":estudiante}

@app.get("/peticion-2")
def peticion_2_wrapper(edad: int,estado: str, estudiante: bool=True):
    return {"edad":edad, "estado":estado, "estudiante":estudiante}

#parámetros del cuerpo de la funcion 
@app.get("/body-1")
def body_1_wrapper(edad: int=Body(gt=0),nombre: str = Body()):
    return{"edad":edad,"nombre":nombre}

