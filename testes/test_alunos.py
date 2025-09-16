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


def test_atualizar_aluno(test_client):
    # Criar aluno primeiro
    aluno_data = {"nome": "Maria", "idade": 30, "plano": "Basic"}
    response = test_client.post("/alunos/", json=aluno_data)
    aluno_id = response.json()["id"]

    # Atualizar aluno
    update_data = {"idade": 31, "plano": "Premium"}
    response = test_client.put(f"/alunos/{aluno_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["idade"] == 31


def test_deletar_aluno(test_client):
    # Criar aluno primeiro
    aluno_data = {"nome": "Pedro", "idade": 22, "plano": "Basic"}
    response = test_client.post("/alunos/", json=aluno_data)
    aluno_id = response.json()["id"]

    # Deletar aluno
    response = test_client.delete(f"/alunos/{aluno_id}")
    assert response.status_code == 200
