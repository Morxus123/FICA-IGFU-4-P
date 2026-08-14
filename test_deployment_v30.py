from fastapi.testclient import TestClient
from main import app

c = TestClient(app)

def test_health():
    r = c.get("/api/health")
    assert r.status_code == 200

def test_final_manifest_is_present():
    r = c.get("/api/final")
    assert r.status_code == 200
    assert r.json()["version"] in {"3.0.0", "3.1.0", "4.0.0"}
