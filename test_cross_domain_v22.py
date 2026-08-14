from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_graph_schema():
    r=c.get("/api/science/graph/schema")
    assert r.status_code==200
    assert "measurement" in r.json()["node_types"]

def test_cross_domain_graph():
    g={"nodes":[
      {"id":"m1","domain":"physics","type":"measurement"},
      {"id":"e1","domain":"mathematics","type":"equation"},
      {"id":"a1","domain":"computer_science","type":"algorithm"},
      {"id":"r1","domain":"statistics","type":"result"}],
      "edges":[
        {"source":"m1","target":"e1","relation":"modeled_by"},
        {"source":"e1","target":"a1","relation":"implemented_by"},
        {"source":"a1","target":"r1","relation":"evaluated_by"}]}
    r=c.post("/api/science/graph/validate",json=g)
    assert r.status_code==200
    assert r.json()["valid"] is True
    assert len(r.json()["domains"])==4
