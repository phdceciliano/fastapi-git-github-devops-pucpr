import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
def clean_database():
    from src.database import alunos_db, treinos_db
    # Limpa os bancos antes de cada teste
    alunos_db.clear()
    treinos_db.clear()
    yield