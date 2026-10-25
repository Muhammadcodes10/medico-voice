from fastapi import FastAPI
app = FastAPI()
@app.get("/voice") 
def voice():
    return {"status": "YOooooooooooooo"}


@app.get("/") 
def voice():
    return {"message": "Medico is running"}