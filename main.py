from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'RnB', 'genre': 'Blues'},
    {'id': 2, 'name': 'West Life', 'genre': 'Western'},
    {'id': 3, 'name': 'Mavin', 'genre': 'Afrobeat'},
]
class GenreURLChoices(Enum):
    BLUES = 'blues'
    WESTERN = 'western'
    AFROBEAT = 'afrobeat'


@app.get('/')
async def index() -> list[str, str]:
    return {"message", "Hello,", "World!"}

@app.get('/about')
async def about() -> str:
    return "An exceptional company"


@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    band_genre = next((g for g in BANDS if g['genre'] == genre), None)
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]