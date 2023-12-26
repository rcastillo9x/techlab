import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_product(client):
    response = client.post('/products', json={'id': 1, 'name': 'Test Product'})
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_read_product(client):
    # Assuming the product with ID 1 exists
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_update_product(client):
    # Assuming the product with ID 1 exists
    response = client.put('/products/1', json={'id': 1, 'name': 'Updated Test Product'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Test Product'

def test_delete_product(client):
    # Assuming the product with ID 1 exists
    response = client.delete('/products/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Product removed'

# Additional tests can be added as needed
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_product(client):
    response = client.post('/products', json={'id': 1, 'name': 'Test Product'})
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_read_product(client):
    # Assuming the product with ID 1 exists
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_update_product(client):
    # Assuming the product with ID 1 exists
    response = client.put('/products/1', json={'id': 1, 'name': 'Updated Test Product'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Test Product'

def test_delete_product(client):
    # Assuming the product with ID 1 exists
    response = client.delete('/products/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Product removed'

# Additional tests can be added as needed
