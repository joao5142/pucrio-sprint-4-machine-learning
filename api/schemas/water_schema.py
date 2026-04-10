from pydantic import BaseModel
from typing import List, Optional


class WaterSchema(BaseModel):
    """ Define como uma nova amostra de agua deve ser representada """
    ph: float = 7.0
    hardness: float = 200.0
    solids: float = 20000.0
    chloramines: float = 7.0
    sulfate: float = 333.0
    conductivity: float = 426.0
    organic_carbon: float = 14.0
    trihalomethanes: float = 66.0
    turbidity: float = 4.0


class WaterViewSchema(BaseModel):
    """ Define como uma amostra de agua sera retornada """
    id: int
    ph: Optional[float]
    hardness: Optional[float]
    solids: Optional[float]
    chloramines: Optional[float]
    sulfate: Optional[float]
    conductivity: Optional[float]
    organic_carbon: Optional[float]
    trihalomethanes: Optional[float]
    turbidity: Optional[float]
    potability: Optional[bool]


class WaterListSchema(BaseModel):
    """ Define como uma lista de amostras sera retornada """
    waters: List[WaterViewSchema]


class WaterSearchSchema(BaseModel):
    """ Define como deve ser a estrutura de busca por ID """
    id: int = 1


class WaterDelSchema(BaseModel):
    """ Define como deve ser a estrutura retornada apos uma remocao """
    message: str
    id: int


def apresenta_water(water):
    """ Retorna uma representacao da amostra seguindo o schema WaterViewSchema """
    return {
        "id": water.id,
        "ph": water.ph,
        "hardness": water.hardness,
        "solids": water.solids,
        "chloramines": water.chloramines,
        "sulfate": water.sulfate,
        "conductivity": water.conductivity,
        "organic_carbon": water.organic_carbon,
        "trihalomethanes": water.trihalomethanes,
        "turbidity": water.turbidity,
        "potability": water.potability,
    }


def apresenta_waters(waters):
    """ Retorna uma representacao da lista de amostras """
    return {"waters": [apresenta_water(w) for w in waters]}
