from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from schemas import *
from flask_cors import CORS
from model import Session, Water, Model, PreProcessador

#  Iniciando a aplicacao Flask com OpenAPI
info = Info(title="Water Quality API", version="1.0.0")
app = OpenAPI(
    __name__, info=info, static_folder="../front", static_url_path="/front"
)
CORS(app)

# Criando tags para agrupamento das rotas
home_tag = Tag(
    name="Documentacao",
    description="Selecao de documentacao: Swagger, Redoc ou RapiDoc",
)
water_tag = Tag(
    name="Agua",
    description="Adicao, listagem e remocao de amostras de agua",
)

MODEL_PATH = "./machine_learning/models/modelo_water.pkl"


@app.get("/", tags=[home_tag])
def home():
    """Redireciona para o frontend."""
    return redirect("/front/index.html")


@app.get("/docs", tags=[home_tag])
def docs():
    """Redireciona para a documentação."""
    return redirect("/openapi")


@app.post("/water", tags=[water_tag],
          responses={"200": WaterViewSchema, "400": ErrorSchema})
def add_water(body: WaterSchema):
    """Adiciona uma nova amostra de agua.

    Realiza a predicao pelo modelo treinado e adiciona no objeto para salvar.
    """
    ml_model = Model()
    ml_model.carrega_modelo(MODEL_PATH)

    preprocessador = PreProcessador()
    X_input = preprocessador.preparar_form(body)
    potability = bool(ml_model.preditor(X_input)[0])

    water = Water(
        ph=body.ph,
        hardness=body.hardness,
        solids=body.solids,
        chloramines=body.chloramines,
        sulfate=body.sulfate,
        conductivity=body.conductivity,
        organic_carbon=body.organic_carbon,
        trihalomethanes=body.trihalomethanes,
        turbidity=body.turbidity,
        potability=potability,
    )

    session = Session()
    try:
        session.add(water)
        session.commit()
        return apresenta_water(water), 200
    except Exception as e:
        session.rollback()
        return {"message": str(e)}, 400
    finally:
        session.close()


@app.get("/waters", tags=[water_tag],
         responses={"200": WaterListSchema, "400": ErrorSchema})
def get_waters():
    """Lista todas as amostras de agua cadastradas."""
    session = Session()
    try:
        waters = session.query(Water).all()
        return apresenta_waters(waters), 200
    finally:
        session.close()


@app.get("/water/<int:id>", tags=[water_tag],
         responses={"200": WaterViewSchema, "400": ErrorSchema})
def get_water(path: WaterPathSchema):
    """Busca uma amostra de agua pelo ID."""
    session = Session()
    try:
        water = session.query(Water).filter(Water.id == path.id).first()
        if not water:
            return {"message": "Amostra nao encontrada."}, 400
        return apresenta_water(water), 200
    finally:
        session.close()

 
@app.delete("/water/<int:id>", tags=[water_tag],
            responses={"200": WaterDelSchema, "400": ErrorSchema})
def delete_water(path: WaterPathSchema):
    """Remove uma amostra de agua pelo ID."""
    session = Session()
    try:
        water = session.query(Water).filter(Water.id == path.id).first()
        if not water:
            return {"message": "Amostra nao encontrada."}, 400
        session.delete(water)
        session.commit()
        return {"message": "Amostra removida.", "id": water.id}, 200
    finally:
        session.close()
# Executando a aplicacao Flask em modo debug
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3001)
