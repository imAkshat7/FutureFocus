# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust to your frontend's origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request model
class Skills(BaseModel):
    skills: List[str]

# Sample career prediction endpoint
@app.post("/predict")
async def predict(skills: Skills):
    print(skills)  # Log received skills
    # Dummy logic for career prediction
    dummy_careers = ["Software Developer", "Data Scientist", "Web Developer", "System Analyst"]
    return {"careers": dummy_careers[:min(5, len(dummy_careers))]}  # Return up to 5 career options
