from fastapi import



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
