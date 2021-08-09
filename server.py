from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from datetime import datetime
from pathlib import Path
from math import sqrt
import numpy as np
import csv
import json
import random

from models import CityModel


app = FastAPI(title="BLE Positioning prototype")

# CORSを無効化
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",)

# 設定ファイル読み込み
cities_list = []
with open("static/config/list_of_cities.csv", encoding="utf_8_sig") as f:
    reader = csv.reader(f)
    for d in reader:
        cities_list.append(CityModel(**{"index": int(d[0]),
                                        "name": str(d[1]),
                                        "lat": float(d[2]),
                                        "lng": float(d[3])}))

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


@app.get("/api/get_random_city")
def get_random_city():
    return random.choice(cities_list)


def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
