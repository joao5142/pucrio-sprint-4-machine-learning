import pytest

from app import app

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

