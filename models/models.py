from pydantic import BaseModel, Field

from typing import Literal


class ZodiacCalculatorRequest(BaseModel):
    birth_date: int = Field(..., description="Date of birth from 1-31", ge=1, le=31)
    birth_month: int = Field(..., description="Month of birth from 1-12", ge=1, le=12)


class DailyPredictionResponse(BaseModel):
    general: Literal["Excellent", "Good", "Neutral", "Challenging", "Difficult"]
    mood_energy: Literal["High", "Moderate", "Low"]
    love: Literal["Favorable", "Stable", "Unfavorable"]
    career: Literal["Progressive", "Stable", "Blocked", "Pressure day", "Opportunity spike"]
    health: Literal["Strong", "Moderate", "Low energy", "Stress-prone", "Rest recommended"]