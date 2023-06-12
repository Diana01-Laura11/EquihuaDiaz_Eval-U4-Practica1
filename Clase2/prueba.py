import requests 

BASE_URL= "http://127.0.0.1:8000"

def peticion_1():
    #respuesta = requests.get(BASE_URL+"/peticion-1?edad=2")
    respuesta = requests.get(BASE_URL+"/peticion-1?",params={
        "edad":21,
        "estado": "Michoacan",
        "estudiante": True, 
    })
    print(respuesta.json())
    
def peticion_2():
    respuesta = requests.get(BASE_URL+"/peticion-2?",params={
        "edad":18,
        "estado": "Michoacan",
        "estudiante": True, 
    })
    print(respuesta.json())
def body_1():
    respuesta = requests.post(BASE_URL+"/body-1",json={
        "edad":20,
        "nombre":"Laura",
    })
    print(respuesta.json())
#peticion_1()
body_1()
