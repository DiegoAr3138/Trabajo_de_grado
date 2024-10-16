from typing import List
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse 
from src.models.movie_models import Movie, MovieCreate, MovieUpdate


movies: List[Movie] =[]

movie_router = APIRouter()

@movie_router.get("/movies" , tags=['Movies'] , status_code=200 , response_description="esto nos debe de devolter algo")
def get_movies() -> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=400)


@movie_router.get("/movies/{id}" , tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})

@movie_router.get("/movies/" , tags=['Movies'])
def get_movie_by_category(category:str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return movie.model_dump()
    return{}


@movie_router.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    #return JSONResponse(content=content)
    return RedirectResponse("/movies", status_code=303)  #esto sirve para rederigir a una pestaña diferente
    #en este caso esto es envia a la seccion movies que es para solicitar la lista de peliculas




@movie_router.put("/movies/{id}", tags=["Movies"])
def update_movie(id:int,movie:MovieUpdate)->List[Movie]:
    for item in movies:
        if item.id == id:
            item.title= movie.title
            item.year= movie.year
            item.overview=movie.overview
            item.rating=movie.rating
            item.category=movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)


@movie_router.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id:int) -> List[Movie]:
    for movie in movies:
        if movie.id == id: 
           movies.remove(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

@movie_router.get('/get_file')
def get_file():
    return FileResponse('Notas.txt')