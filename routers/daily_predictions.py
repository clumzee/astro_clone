import random

from fastapi import APIRouter
from models.models import DailyPredictionResponse
from LLM.openai import llm, template

router = APIRouter()


@router.get("/daily_predictions")
async def calculate_variables(zodiac_sign: str):
    
    return DailyPredictionResponse(
        general=random.choice(["Excellent", "Good", "Neutral", "Challenging", "Difficult"]),
        mood_energy=random.choice(["High", "Moderate", "Low"]),
        love=random.choice(["Favorable", "Stable", "Unfavorable"]),
        career=random.choice(["Progressive", "Stable", "Blocked", "Pressure day", "Opportunity spike"]),
        health=random.choice(["Strong", "Moderate", "Low energy", "Stress-prone", "Rest recommended"])
    )

@router.get("/predict_horoscope")
async def predict_horoscope(zodiac_sign: str):
    
    variables = DailyPredictionResponse(
        general=random.choice(["Excellent", "Good", "Neutral", "Challenging", "Difficult"]),
        mood_energy=random.choice(["High", "Moderate", "Low"]),
        love=random.choice(["Favorable", "Stable", "Unfavorable"]),
        career=random.choice(["Progressive", "Stable", "Blocked", "Pressure day", "Opportunity spike"]),
        health=random.choice(["Strong", "Moderate", "Low energy", "Stress-prone", "Rest recommended"])
    )


    prompt = template.format(variables=variables.json())
    response = llm.invoke(prompt)

    return {"Horoscope":response.content}
