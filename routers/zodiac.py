from fastapi import APIRouter
from models.models import ZodiacCalculatorRequest

router = APIRouter()


@router.post("/calculate_zodiac")
async def calculate_zodiac(request: ZodiacCalculatorRequest):
    birth_date = int(request.birth_date)
    birth_month = int(request.birth_month)

    signs = [
        ("Capricorn", (1, 1), (1, 19)),
        ("Aquarius",  (1, 20), (2, 18)),
        ("Pisces",    (2, 19), (3, 20)),
        ("Aries",     (3, 21), (4, 19)),
        ("Taurus",    (4, 20), (5, 20)),
        ("Gemini",    (5, 21), (6, 20)),
        ("Cancer",    (6, 21), (7, 22)),
        ("Leo",       (7, 23), (8, 22)),
        ("Virgo",     (8, 23), (9, 22)),
        ("Libra",     (9, 23), (10, 22)),
        ("Scorpio",   (10, 23), (11, 21)),
        ("Sagittarius",(11,22),(12,21)),
        ("Capricorn", (12,22), (12,31))
    ]


    for sign, start, end in signs:
        if (birth_month, birth_date) >= start and (birth_month, birth_date) <= end:
            return {"zodiac_sign": sign}
    return {"zodiac_sign": None}