from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_apply():
    r=c.post("/api/function/apply",json={"function":"double","input":4})
    assert r.json()["output"]==8

def test_composition():
    r=c.post("/api/function/compose",json={"first":"double","second":"square","input":3})
    assert r.json()["output"]==36
    assert r.json()["expression"]=="square∘double"
