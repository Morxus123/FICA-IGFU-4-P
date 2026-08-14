from fastapi.testclient import TestClient
from main import app
c=TestClient(app)

CASES=[
 ("mathematics","gcd",{"a":84,"b":30},6),
 ("computer_information_sciences","graph_stats",{"nodes":[1,2,3],"edges":[[1,2],[2,3]]},3),
 ("physical_sciences","kinetic_energy",{"mass_kg":2,"velocity_m_s":3},9),
 ("chemical_sciences","molarity",{"moles":2,"volume_l":1},2),
 ("earth_environmental_sciences","temperature_anomaly",{"observed":12,"baseline":10},2),
 ("biological_sciences","exponential_growth",{"initial":100,"rate":0.1,"periods":1},110),
 ("engineering_technology","stress",{"force":100,"area":2},50),
 ("medical_health_sciences","bmi",{"weight_kg":80,"height_m":2},20),
 ("agricultural_veterinary_sciences","yield_per_area",{"output":100,"area":5},20),
 ("social_sciences","mean",{"values":[1,2,3]},2),
]

def test_engines_registry():
    r=c.get("/api/science/engines")
    assert r.status_code==200
    assert len(r.json()["engines"])>=10

def test_representative_engines():
    for domain,op,payload,expected in CASES:
        r=c.post("/api/science/engine/run",
                 json={"domain":domain,"operation":op,"payload":payload})
        assert r.status_code==200, (domain,op,r.text)
        value=list(r.json()["result"].values())[0]
        assert abs(value-expected) < 1e-9 if isinstance(value,(int,float)) and isinstance(expected,(int,float)) else value==expected, (domain,op,value,expected)

def test_humanities_engine():
    r=c.post("/api/science/engine/run",json={
        "domain":"humanities_arts","operation":"argument_structure_check",
        "payload":{"premises":["P1"],"conclusion":"C"}})
    assert r.status_code==200
    assert r.json()["result"]["valid"] is True
