from sqlalchemy import Boolean, Column, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from model import Base


class Water(Base):
    __tablename__ = 'waters'

    id = Column(Integer, primary_key=True)
    ph = Column("ph", Float)
    hardness = Column("Hardness", Float)
    solids = Column("Solids", Float)
    chloramines = Column("Chloramines", Float)
    sulfate = Column("Sulfate", Float)
    conductivity = Column("Conductivity", Float)
    organic_carbon = Column("Organic_carbon", Float)
    trihalomethanes = Column("Trihalomethanes", Float)
    turbidity = Column("Turbidity", Float)
    potability = Column("Potability", Boolean)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, ph: float, hardness: float, solids: float,
                 chloramines: float, sulfate: float, conductivity: float,
                 organic_carbon: float, trihalomethanes: float, turbidity: float,
                 potability: bool,
                 created_at: Union[DateTime, None] = None):
        """
        Cria uma amostra de água.
        """
        self.ph = ph
        self.hardness = hardness
        self.solids = solids
        self.chloramines = chloramines
        self.sulfate = sulfate
        self.conductivity = conductivity
        self.organic_carbon = organic_carbon
        self.trihalomethanes = trihalomethanes
        self.turbidity = turbidity
        self.potability = potability

        if created_at:
            self.created_at = created_at
