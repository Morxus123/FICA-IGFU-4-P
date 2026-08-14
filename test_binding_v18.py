from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_binding():
    r=c.post("/api/binding/validate",json={"variable":"x","value":42})
    assert r.json()["valid"] is True

def test_substitution():
    r=c.post("/api/binding/substitute",json={
        "expression":"x + 0","bindings":{"x":42}})
    assert r.json()["substituted"]=="42 + 0"
    assert r.json()["normal_form"]=="42"

def test_identifier_boundary():
    r=c.post("/api/binding/substitute",json={
        "expression":"xx + x","bindings":{"x":42}})
    assert r.json()["substituted"]=="xx + 42"
