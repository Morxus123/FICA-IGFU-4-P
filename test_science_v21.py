from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_domains():
    r=c.get("/api/science/domains")
    assert r.status_code==200
    assert "physics" in r.json()["domains"]
    assert "biology" in r.json()["domains"]

def test_model_validation():
    r=c.post("/api/science/model/validate",json={
        "domain":"physics","model":{"name":"demo","variables":["x","t"]}})
    assert r.status_code==200
    assert r.json()["valid"] is True
    assert r.json()["scientific_truth_proved"] is False
