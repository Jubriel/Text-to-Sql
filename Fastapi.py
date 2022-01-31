# importing libraries
from fastapi import FastAPI
import uvicorn
import joblib, os
from pydantic import BaseModel
import tableqa
import psycopg2
from TableQA import text2sql

# Initializing required modules and models
app = FastAPI()

@app.get('/')
async def index():
    return "Text to sql Analytics"

class features(BaseModel):
    schema: str
    question: str
    

# Price Prediction
@app.post('/predict')
async def predict_price(data: features):

    return text2sql(data['schema'], data['question'])
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port = 8080)