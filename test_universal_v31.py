from fastapi.testclient import TestClient
from main import app

c = TestClient(app)

def test_universal_registry():
    r = c.get("/api/operators/universal")
    assert r.status_code == 200
    ops = r.json()["operators"]
    assert "add" in ops
    assert "multiply" in ops
    assert r.json()["application_modules"]["collatz"]["status"] == "application"

def test_universal_apply():
    r = c.post("/api/operators/apply",
               json={"operator":"multiply","args":[6,7]})
    assert r.status_code == 200
    assert r.json()["result"] == 42
    assert r.json()["certificate"]["theorem_proved"] is False

def test_non_collatz_application():
    r = c.post("/api/operators/apply",
               json={"operator":"square","args":[9]})
    assert r.status_code == 200
    assert r.json()["result"] == 81
