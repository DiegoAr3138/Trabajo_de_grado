from fastapi import FastAPI, Body , Path , Query
from fastapi.responses import HTMLResponse , JSONResponse, PlainTextResponse, RedirectResponse , FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime

app = FastAPI()


app.title = "Mi primer aplicacion"
app.version = "1.0"


@app.get("/" , tags=['Home'])
def home():
    return PlainTextResponse(content="Home")