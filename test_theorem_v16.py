from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_theorem_validation():
    t={"id":"T001","statement":"Every element equals 7.","assumptions":[],"obligations":[]}
    r=c.post("/api/theorem/validate",json=t)
    assert r.status_code==200
    assert r.json()["status"]=="proposed"

def test_theorem_discharge():
    t={"id":"T002","statement":"Every element of D equals 7.","assumptions":[],
       "obligations":[{"kind":"finite_quantifier","quantifier":{
           "kind":"forall","variable":"x","domain":[7,7,7],
           "predicate":{"op":"equals","value":7}}}]}
    r=c.post("/api/theorem/discharge",json=t)
    assert r.status_code==200
    assert r.json()["status"]=="verified_derivation"
    assert r.json()["theorem_proved"] is False

def test_failed_obligation():
    t={"id":"T003","statement":"Bad finite claim","assumptions":[],
       "obligations":[{"kind":"finite_quantifier","quantifier":{
           "kind":"forall","variable":"x","domain":[7,8],
           "predicate":{"op":"equals","value":7}}}]}
    r=c.post("/api/theorem/discharge",json=t)
    assert r.json()["status"]=="obligations_open"
