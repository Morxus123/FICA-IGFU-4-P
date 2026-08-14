from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_reflexivity():
    r=c.post("/api/inference/check",json={"rule":"EQ_REFL","x":42}).json()
    assert r["valid"] is True
    assert r["conclusion"] == {"left":42,"right":42}

def test_symmetry():
    r=c.post("/api/inference/check",json={"rule":"EQ_SYM","left":"a","right":"b"}).json()
    assert r["valid"] is True
    assert r["conclusion"] == {"left":"b","right":"a"}

def test_divisibility():
    r=c.post("/api/inference/check",json={"rule":"DIVISIBLE","a":28,"b":7}).json()
    assert r["valid"] is True
