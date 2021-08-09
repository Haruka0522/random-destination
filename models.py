from pydantic import BaseModel


class CityModel(BaseModel):
    index: int
    name: str
    lat: float
    lng: float
