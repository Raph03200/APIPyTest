import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def teste_nome_vazio(client):
    response = client.get('/nomes')
    assert response.status_code == 200
    assert response.get_json() == []

def teste_adicionar_nome(client):
    response = client.post('/nomes', json={'name': 'Raphael'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Raphael'
    assert 'id' in data

def teste_nome_sem_name(client):
    response = client.post('/nomes', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()
