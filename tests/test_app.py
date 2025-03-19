import pytest
from main import app

@pytest.fixture
def client():
    """Créer un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test de la route principale."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World'

def test_500_error(client):
    """Simuler une erreur interne pour tester le handler 500."""
    # Effectuer une requête pour cette route qui va provoquer une erreur
    response = client.get('/error')

    # Vérifier que le gestionnaire d'erreurs renvoie bien un code 500 et un message d'erreur
    assert response.status_code == 500
    assert b'An internal error occurred' in response.data
