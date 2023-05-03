import pytest

def test_get_all_planets(client, two_planets):
    response = client.get("/planet")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body ==[{
        "id": 1,
        "name": "Mars",
        "description": "Fourth planet from the Sun",
        "moons": 2,
        "color": "Brown"
    },
    {
        "id": 2,
        "name": "Venus",
        "description": "Second planet from the Sun",
        "moons": 0,
        "color": "Orange"
    }]

def test_post_creates_restaurant(client):
    response = client.post("/planet", json={
        "name": "Mars",
        "description": "Fourth planet from the Sun",
        "moons": 2,
        "color": "Brown"
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body

def test_delete_planet(client, two_planets):
    response = client.delete("/planet/2")
    
    response_body = response.get_json()

    assert response.status_code == 200
    assert "planet 2 successfully deleted" in response_body["msg"]

def test_put_planet(client, two_planets):
    response = client.put("/planet/1", json={
        "name": "Earth",
        "description": "Home",
        "moons": 1,
        "color": "multi"
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert "planet 1 successfully updated" in response_body["msg"]
