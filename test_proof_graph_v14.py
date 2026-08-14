from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_valid_graph():
    g={"nodes":[
        {"id":"n1","rule":"ASSUMPTION","depends_on":[]},
        {"id":"n2","rule":"EQ_REFL","depends_on":["n1"],
         "inference":{"rule":"EQ_REFL","x":42}}
    ],"conclusion":"n2"}
    r=c.post("/api/proof/graph/verify",json=g)
    assert r.status_code==200
    assert r.json()["status"]=="verified_derivation"

def test_missing_dependency_rejected():
    g={"nodes":[{"id":"n1","rule":"ASSUMPTION","depends_on":["missing"]}]}
    r=c.post("/api/proof/graph/verify",json=g)
    assert r.json()["status"]=="rejected"
