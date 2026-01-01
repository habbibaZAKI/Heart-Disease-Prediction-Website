from fastapi import FastAPI

app = FastAPI(title="Heart Disease Prediction API")

@app.get("/")
def root():
    return {"message": "Backend is running successfully"}
