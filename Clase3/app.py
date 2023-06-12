import uvicorn
from fastapi import FastAPI
from BankNotes import BankNotes
import  numpy as np 
import pickle
import pandas as pd 


app = FastAPI()
pickle_in = open("classifer.pk1","rb")
classifer=pickle.load(pickle_in)

@app.get("/Bienvenida")
def fun_nombre(name:str):
    return{"Hola bienvennido":f"{name}"}

@app.post("/predict")
def predict_banknote(data:BankNotes):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    
    prediction = classifer.predict([[variance,skewness,curtosis,entropy]])  
    
    if(prediction[0]>0.5):
        prediction = "Nota falsa"
    else:
        prediction = "Es una nota de Banco" 
        
    return{"prediction":prediction} 