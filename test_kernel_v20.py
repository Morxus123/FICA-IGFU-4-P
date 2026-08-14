from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

def test_kernel_online():
    r=c.get("/api/kernel")
    assert r.status_code==200
    assert r.json()["version"]=="2.0.0"

def test_state_validation():
    obj={"kind":"state","id":"x","domain":"integer","value":42}
    r=c.post("/api/kernel/validate",json=obj)
    assert r.json()["valid"] is True
    assert r.json()["kind"]=="state"

def test_certificate():
    obj={"kind":"proposition","statement":"P(42)","assumptions":[]}
    r=c.post("/api/kernel/certificate",json=obj)
    assert r.status_code==200
    assert "certificate" in r.json()
    assert r.json()["certificate"]["theorem_proved"] is False
