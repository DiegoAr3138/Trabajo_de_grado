from fastapi import FastAPI, Body , Path , Query
from fastapi.responses import HTMLResponse , JSONResponse, PlainTextResponse, RedirectResponse , FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime

app = FastAPI()

class Movie(BaseModel):
    id: int
    title:str 
    overview:str
    year:int
    rating:float
    category:str

class MovieCreate(BaseModel):
    id: int
    title:str#= Field(min_length=5, max_length=15, default="Titulo")
    overview:str = Field(min_length=15, max_length=50, default= "Descripcion")
    year:int = Field(le=datetime.date.today().year, ge=1900)
    rating:float
    category:str = Field(min_length=5, max_length=15)
    
    model_config = {
        'json_schema_extra':{
            'example' : {
                'id' : 1,
                "title" : "Titulo",
                "overview": "Descripcion de la pelicula",
                "year" : 1990,
                "rating": 0.0,
                "category": "accion"
            }
        }
    }
    
    @validator("title")
    def validate_title(cls, value):
        if len(value)<5:
            raise ValueError("EL titutlo debe tener como minimo 5 caracteres")
        if len(value)>15:
            raise ValueError("EL titutlo debe tener como maximo 15 caracteres")
        return value


class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int
    rating:float
    category:str


movies: List[Movie] =[]

app.title = "Mi primer aplicacion"
app.version = "1.0"


@app.get("/" , tags=['Home'])
def home():
    return PlainTextResponse(content="Home")




@app.get("/movies" , tags=['Movies'] , status_code=200 , response_description="esto nos debe de devolter algo")
def get_movies() -> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=400)


@app.get("/movies/{id}" , tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})


@app.get("/movies/" , tags=['Movies'])
def get_movie_by_category(category:str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return movie.model_dump()
    return{}


@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    #return JSONResponse(content=content)
    return RedirectResponse("/movies", status_code=303)  #esto sirve para rederigir a una pestaña diferente
    #en este caso esto es envia a la seccion movies que es para solicitar la lista de peliculas




@app.put("/movies/{id}", tags=["Movies"])
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


@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id:int) -> List[Movie]:
    for movie in movies:
        if movie.id == id: 
           movies.remove(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

@app.get('/get_file')
def get_file():
    return FileResponse('Notas.txt')