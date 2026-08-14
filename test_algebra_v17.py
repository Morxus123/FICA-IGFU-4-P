from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_normalize_add_zero():
    r=c.post("/api/algebra/normalize",json={"expression":"x + 0"})
    assert r.json()["normal_form"]=="x"

def test_equivalent():
    r=c.post("/api/algebra/equivalent",json={"left":"x + 0","right":"x"})
    assert r.json()["equivalent"] is True

def test_non_equivalent():
    r=c.post("/api/algebra/equivalent",json={"left":"x + 0","right":"x+1"})
    assert r.json()["equivalent"] is False
