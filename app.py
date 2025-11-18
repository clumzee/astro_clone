import csv

from io import StringIO

import jwt
from fastapi import (APIRouter, Depends, FastAPI, File, HTTPException, Security,
                     UploadFile)

from routers import zodiac_router, daily_predictions_router





app = FastAPI()


@app.get("/health")
async def root():

    return {"status": "ok"}


app.include_router(zodiac_router, prefix="/zodiac", tags=["zodiac"])
app.include_router(daily_predictions_router, prefix="/predictions", tags=["predictions"])