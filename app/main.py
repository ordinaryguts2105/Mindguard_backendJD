from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{username}")
async def root(username: str):

    score = random.randint(0, 100)

    if score >= 80:
        message = f"{username}, you're performing at peak balance today."
        status = "Excellent"
        tip = "Keep maintaining your healthy rhythm."

    elif score >= 60:
        message = f"You're holding steady, {username}."
        status = "Stable"
        tip = "A calm evening routine can improve tomorrow."

    elif score >= 40:
        message = f"{username}, some stress patterns detected today."
        status = "Moderate"
        tip = "Take short breaks and reduce screen exposure."

    elif score >= 20:
        message = f"{username}, wellness signals show fatigue buildup."
        status = "Warning"
        tip = "Prioritize rest and avoid late-night scrolling."

    else:
        message = f"{username}, critical wellness state detected."
        status = "Critical"
        tip = "Consider reaching out to a trusted guardian."

    return {
        "username": username,
        "message": message,
        "score": score,
        "status": status,
        "tip": tip
    }
