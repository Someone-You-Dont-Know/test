"""Tests for the FastAPI app."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_say_hello():
    """Test the / endpoint returns the expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
