import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_accueil(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "auteur" in data
    assert data["auteur"] == "Jihene Zgolli"

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_skills(client):
    response = client.get('/skills')
    assert response.status_code == 200
    data = response.get_json()
    assert "competences" in data
    assert "telecom" in data["competences"]

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert "version" in data
