import pytest
from fastapi.testclient import TestClient
from patientsmanagement import app

client = TestClient(app)

NEW_PATIENT = {
    "id": "p100",
    "name": "Test Person",
    "city": "Denver",
    "age": 30,
    "gender": "Female",
    "height_m": 1.65,
    "weight_kg": 60.0,
    "bmi": 22.0,
    "verdict": "Normal weight",
}


@pytest.fixture
def restore_data():
    with open("patients.json", "r") as f:
        original = f.read()
    yield
    with open("patients.json", "w") as f:
        f.write(original)


def test_list_patients():
    response = client.get("/patient")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_one_patient():
    response = client.get("/patient/p003")
    assert response.status_code == 200
    assert response.json()["id"] == "p003"


def test_get_missing_patient():
    response = client.get("/patient/p999")
    assert response.status_code == 404


def test_sort_by_age():
    response = client.get("/sort", params={"sort_by": "age"})
    assert response.status_code == 200
    ages = [patient["age"] for patient in response.json()]
    assert ages == sorted(ages)


def test_sort_invalid_field():
    response = client.get("/sort", params={"sort_by": "banana"})
    assert response.status_code == 400


def test_create_patient(restore_data):
    response = client.post("/create", json=NEW_PATIENT)
    assert response.status_code == 200

    response = client.get("/patient/p100")
    assert response.status_code == 200


def test_create_duplicate(restore_data):
    duplicate = NEW_PATIENT.copy()
    duplicate["id"] = "p003"
    response = client.post("/create", json=duplicate)
    assert response.status_code == 400


def test_create_missing_field(restore_data):
    missing_age = NEW_PATIENT.copy()
    del missing_age["age"]
    response = client.post("/create", json=missing_age)
    assert response.status_code == 422


def test_update_patient(restore_data):
    original_name = client.get("/patient/p003").json()["name"]

    response = client.put("/patient/p003", json={"city": "Boston"})
    assert response.status_code == 200

    patient = client.get("/patient/p003").json()
    assert patient["city"] == "Boston"
    assert patient["name"] == original_name


def test_delete_patient(restore_data):
    response = client.delete("/patient/p003")
    assert response.status_code == 200

    response = client.get("/patient/p003")
    assert response.status_code == 404


def test_delete_missing(restore_data):
    response = client.delete("/patient/p999")
    assert response.status_code == 404
