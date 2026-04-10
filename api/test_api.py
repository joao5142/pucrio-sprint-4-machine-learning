import pytest
import json
from app import app
from model import Session, Water

@pytest.fixture
def client():
    """Configura o cliente de teste para a aplicação Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_redirect(client):
    """Testa redirecionamento para o frontend"""
    response = client.get('/')
    
    assert response.status_code == 302
    assert '/front/index.html' in response.location

def test_docs_redirect(client):
    """Testa redirecionamento para a documentação OpenAPI"""
    response = client.get('/docs')

    assert response.status_code == 302
    assert '/openapi' in response.location

@pytest.fixture
def sample_water_data():
    """Dados de exemplo para teste de água"""
    return {
        "ph": 7.0,
        "hardness": 100,
        "solids": 100,
        "chloramines": 100,
        "sulfate": 100,
        "conductivity": 100,
        "organic_carbon": 100,
        "trihalomethanes": 100,
        "turbidity": 100,
    }

def test_add_water_prediction(client, sample_water_data):
    """Testa a adição de um amostra de água com predição"""

    response = client.post('/water', 
                          data=json.dumps(sample_water_data),
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    
    # Verifica se a amostra de água foi criado com todas as informações
    assert data['ph'] == sample_water_data['ph']
    assert data['hardness'] == sample_water_data['hardness']
    assert data['solids'] == sample_water_data['solids']
    assert data['chloramines'] == sample_water_data['chloramines']
    assert data['sulfate'] == sample_water_data['sulfate']
    assert data['conductivity'] == sample_water_data['conductivity']
    assert data['organic_carbon'] == sample_water_data['organic_carbon']
    assert data['trihalomethanes'] == sample_water_data['trihalomethanes']
    assert data['turbidity'] == sample_water_data['turbidity']


    # Verifica se a predição foi feita (potability deve estar presente)
    assert 'potability' in data
    assert data['potability'] in [0, 1]  # Deve ser 0 (não potável) ou 1 (potável)

def test_get_water_by_id(client, sample_water_data):
    """Testa a busca de um amostra de água por id"""
    # Primeiro adiciona a água
    response_add = client.post('/water',
                data=json.dumps(sample_water_data),
                content_type='application/json')
    
    data = json.loads(response_add.data)
    water_id = data['id']
    
    # Busca o paciente por id
    response = client.get(f'/water/{water_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == water_id

def test_delete_water(client, sample_water_data):
    """Testa a remoção de uma água"""
    # Primeiro adiciona
    response_add = client.post('/water',
                data=json.dumps(sample_water_data),
                content_type='application/json')
    
    data = json.loads(response_add.data)
    water_id = data['id']

    # Remove pelo id
    response = client.delete(f'/water/{water_id}')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Amostra removida."

def cleanup_test_water():
    """Limpa amostras de água de teste do banco"""
    session = Session()
    test_waters = session.query(Water).filter(
        Water.ph == 7.0,
        Water.hardness == 100,
        Water.solids == 100
    ).all()
    
    for water in test_waters:
        session.delete(water)
    session.commit()
    session.close()

# Executa limpeza após os testes
def test_cleanup():
    """Limpa dados de teste"""
    cleanup_test_water()
