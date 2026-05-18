from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_add_and_look_dictionary():
    response = client.post("/dictionary/new-entry", json={
        "word": "Apple",
        "definition": "A fruit that grows on trees"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Added word 'Apple' successfully."}

    response = client.get("/dictionary/look/Apple")
    assert response.status_code == 200
    assert response.json() == {"definition": "A fruit that grows on trees"}

    response = client.get("/dictionary/look/Banana")
    assert response.status_code == 200
    assert "Can't find entry for Banana" in response.json()["definition"]

def test_shopping_total():
    response = client.post("/shopping/total", json={
        "costs": {"socks": 5, "shoes": 60, "sweater": 30},
        "items": ["socks", "shoes"],
        "tax": 0.09
    })
    assert response.status_code == 200
    assert response.json()["total"] == 70.85

    response = client.post("/shopping/total", json={
        "costs": {"socks": 5},
        "items": ["hat", "socks"],
        "tax": 0.1
    })
    assert response.json()["total"] == 5.50

def test_concatenate_endpoint():
    response = client.post("/words/concatenate", json={
        "words": ["yoda", "best", "has"]
    })
    assert response.status_code == 200
    assert response.json()["result"] == "yes"

    response = client.post("/words/concatenate", json={
        "words": ["apple", "banana", "cherry", "date"]
    })
    assert response.json()["result"] == "aaee"

    response = client.post("/words/concatenate", json={"words": []})
    assert response.json()["result"] == ""