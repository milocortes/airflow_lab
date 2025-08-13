from fastapi import FastAPI
import random 
# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"valor" : random.uniform(200, 600)}