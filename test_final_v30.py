from fastapi.testclient import TestClient
from main import app

c=TestClient(app)

def test_final_manifest():
    r=c.get("/api/final")
    assert r.status_code == 200
    assert r.json()["version"] in {"3.0.0", "3.1.0", "4.0.0"}
    assert "physics" in r.json()["scope"]

def test_audit_status():
    r=c.get("/api/audit/status")
    assert r.status_code == 200
    assert r.json()["status"] == "operational_prototype"

def test_measurement():
    r=c.post("/api/measurement/validate",
             json={"value":10.0,"unit":"m","uncertainty":0.1})
    assert r.status_code == 200
    assert r.json()["valid"] is True

def test_uncertainty_addition():
    r=c.post("/api/measurement/add",json={
        "a":{"value":10.0,"unit":"m","uncertainty":0.1},
        "b":{"value":5.0,"unit":"m","uncertainty":0.2}})
    assert r.status_code == 200
    assert abs(r.json()["result"]["value"]-15.0) < 1e-12
    assert r.json()["result"]["uncertainty"] > 0.2

def test_unit_mismatch_rejected():
    r=c.post("/api/measurement/add",json={
        "a":{"value":10.0,"unit":"m","uncertainty":0.1},
        "b":{"value":5.0,"unit":"s","uncertainty":0.2}})
    assert r.status_code == 400
