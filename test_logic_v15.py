from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_logic_types():
    r=c.get("/api/logic/types")
    assert r.status_code==200
    assert "theorem" in r.json()["types"]

def test_finite_forall():
    q={"kind":"forall","variable":"x","domain":[7,7,7],
       "predicate":{"op":"equals","value":7}}
    r=c.post("/api/logic/quantifier/check",json=q)
    assert r.status_code==200
    assert r.json()["satisfied"] is True
    assert r.json()["theorem_proved"] is False

def test_finite_exists():
    q={"kind":"exists","variable":"x","domain":[1,2,7],
       "predicate":{"op":"equals","value":7}}
    r=c.post("/api/logic/quantifier/check",json=q)
    assert r.json()["satisfied"] is True
