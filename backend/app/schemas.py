from pydantic import BaseModel, ConfigDict


class Continent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    continent_id: int
    continent_name: str



class Country(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    country_id: int
    country_name: str

