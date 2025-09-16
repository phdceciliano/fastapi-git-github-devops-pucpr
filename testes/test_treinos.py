def test_criar_treino(test_client):
    # Primeiro cria aluno
    aluno_data = {"nome": "Ana", "idade": 28, "plano": "Premium"}
    aluno_response = test_client.post("/alunos/", json=aluno_data)
    aluno_id = aluno_response.json()["id"]

    # Cria treino
    treino_data = {
        "aluno_id": aluno_id,
        "tipo": "Musculação",
        "exercicios": ["Supino"],
        "duracao_minutos": 60
    }
    response = test_client.post("/treinos/", json=treino_data)
    assert response.status_code == 200


def test_criar_treino_aluno_inexistente(test_client):
    treino_data = {
        "aluno_id": "inexistente",
        "tipo": "Musculação",
        "exercicios": ["Supino"],
        "duracao_minutos": 60
    }
    response = test_client.post(
        "/treinos/",
        json=treino_data)
    assert response.status_code == 404
