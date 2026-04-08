from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from schemas import *
from flask_cors import CORS

#  Iniciando a aplicação Flask com OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(
    __name__, info=info, static_folder="../front", static_url_path="/front"
)
CORS(app)

# Criando tags para agrupamento das rotas
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)

# Redirecionando para o frontend
@app.get("/", tags=[home_tag])
def home():
    """Redireciona para o frontend."""
    return redirect("/front/index.html")


# Rota de documentação OpenAPI para Swagger, Redoc ou RapiDoc
@app.get("/docs", tags=[home_tag])
def docs():
    """Redireciona para a documentação OpenAPI."""
    return redirect("/openapi")

# Executando a aplicação Flask em modo debug
if __name__ == "__main__":
    app.run(debug=True)
