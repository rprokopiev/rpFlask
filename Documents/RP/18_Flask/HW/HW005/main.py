'''
Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по заданному жанру.
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс Movie с полями id, title, description и genre.
- Создайте список movies для хранения фильмов.
- Создайте маршрут для получения списка фильмов по жанру (метод GET).
- Реализуйте валидацию данных запроса и ответа.
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
async def root():
    return 'API для получения списка фильмов по жанру'


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str
    status: bool


movies = []


@app.get("/movies/", response_model=list[Movie])
async def read_movies():
    logging.info('<<< GET request >>>')
    return movies


@app.get("/movie/{movie_genre}", response_model=list[Movie])
async def read_genre_movies(movie_genre: str):
    tmp = []
    for movie in movies:
        if movie.genre == movie_genre: 
            tmp.append(movie)
    logging.info('<<< GET request >>>')
    return tmp


@app.post("/movie/", response_model=Movie)
async def add_movie(movie: Movie):
    movies.append(movie)
    logging.info('<<< POST request >>>')
    return movie

