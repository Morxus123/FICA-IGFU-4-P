from fastapi.testclient import TestClient
from main import app

c = TestClient(app)

def test_all_domains():
    r = c.get("/api/science/all-domains")
    assert r.status_code == 200
    data = r.json()
    assert len(data["domains"]) >= 10
    assert "medical_health_sciences" in data["domains"]
    assert "humanities_arts" in data["domains"]

def test_chemistry_object():
    r = c.post("/api/science/domain/operate", json={
        "domain":"chemical_sciences",
        "operation":"validate_object",
        "payload":{"type":"reaction","equation":"A -> B"}
    })
    assert r.status_code == 200
    assert r.json()["result"]["valid"] is True

def test_biology_object():
    r = c.post("/api/science/domain/operate", json={
        "domain":"biological_sciences",
        "operation":"validate_object",
        "payload":{"type":"gene","name":"demo"}
    })
    assert r.status_code == 200
    assert r.json()["result"]["valid"] is True

def test_humanities_object():
    r = c.post("/api/science/domain/operate", json={
        "domain":"humanities_arts",
        "operation":"validate_object",
        "payload":{"type":"text","title":"demo"}
    })
    assert r.status_code == 200
    assert r.json()["result"]["valid"] is True

def test_coverage_is_honest():
    r = c.get("/api/science/coverage")
    assert r.status_code == 200
    assert r.json()["fully_automated_every_subfield"] is False
