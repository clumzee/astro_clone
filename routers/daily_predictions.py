import random

from fastapi import APIRouter
from models.models import DailyPredictionResponse

router = APIRouter()


@router.get("/daily_predictions")
async def calculate_zodiac(zodiac_sign: str):
    
    return DailyPredictionResponse(
        general=random.choice(["Excellent", "Good", "Neutral", "Challenging", "Difficult"]),
        mood_energy=random.choice(["High", "Moderate", "Low"]),
        love=random.choice(["Favorable", "Stable", "Unfavorable"]),
        career=random.choice(["Progressive", "Stable", "Blocked", "Pressure day", "Opportunity spike"]),
        health=random.choice(["Strong", "Moderate", "Low energy", "Stress-prone", "Rest recommended"])
    )
