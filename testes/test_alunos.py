def test_criar_aluno(test_client):
    aluno_data = {"nome": "João Silva", "idade": 25, "plano": "Premium"}
    response = test_client.post("/alunos/", json=aluno_data)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João Silva"
    assert "id" in data

def test_listar_alunos(test_client):
    response = test_client.get("/alunos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_aluno_inexistente(test_client):
    response = test_client.get("/alunos/999")
    assert response.status_code == 404