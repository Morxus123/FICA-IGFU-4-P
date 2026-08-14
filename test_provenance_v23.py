from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_provenance_record():
    r=c.post("/api/provenance/validate",json={"id":"s1","type":"source","metadata":{"title":"demo"}})
    assert r.status_code==200
    assert r.json()["valid"] is True

def test_provenance_chain():
    chain=[
      {"id":"s1","type":"source"},
      {"id":"d1","type":"dataset","derived_from":["s1"]},
      {"id":"m1","type":"measurement","derived_from":["d1"]},
      {"id":"t1","type":"transformation","derived_from":["m1"]},
      {"id":"r1","type":"result","derived_from":["t1"]},
      {"id":"c1","type":"claim","derived_from":["r1"]}]
    r=c.post("/api/provenance/chain/validate",json={"chain":chain})
    assert r.status_code==200
    assert r.json()["valid"] is True

def test_broken_chain():
    r=c.post("/api/provenance/chain/validate",json={"chain":[
      {"id":"r1","type":"result","derived_from":["missing"]}]})
    assert r.json()["valid"] is False
