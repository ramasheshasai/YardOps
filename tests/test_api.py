import pytest

def test_create_site(client):
    response = client.post("/api/sites",json ={
        "name": "test_rama",
        "address": "vijayawada"
    })
    data = response.get_json()
    assert response.status_code == 201
    assert data["name"] == "test_rama"

def test_create_refer_trailer(client):
    response = client.post("/api/trailers",json ={
        "trailer_type": "REFER",
        "trailer_number": "1234",
        "carrier_name": "ABC",
        "temp_setting": 5
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["trailer_type"] == "REFER"
    assert data["temp_setting"] == 5

def test_checkin(client):
    site = client.post("/api/sites", json ={
        "name":"test_rama",
        "address":"Vijayawada"
        }).get_json()
    
    client.post(f"/api/sites/{site['id']}/spots", json={
        "spot_label": "A1"
    })

    trailer = client.post("/api/trailers",json ={
        "trailer_type":"REEFER",
        "trailer_number" : "1234",
        "carrier_name":"ABC"
    }).get_json()

    res = client.post("/appointments/checkin", json={
        "site_id": site["id"],
        "trailer_id": trailer["id"]
    })
    assert res.status_code == 201
    data = res.get_json()

    assert "gate_pass" in data

def test_checkout_free(client):
    site = client.post("/api/sites",json ={
        "name":"test_rama",
        "address":"Vijayawada"
    }).get_json()
    client.post(f"/api/sites/{site['id']}/spots", json={
        "spot_label": "A1"
    })
    trailer = client.post("/api/trailers",json ={
        "trailer_type":"REEFER",
        "trailer_number" : "1234",
        "carrier_name":"ABC"
    }).get_json()
    checkin = client.post("/appointments/checkin", json={
        "site_id": site["id"],
        "trailer_id": trailer["id"]
    }).get_json()
    res = client.post(f"/appointments/{checkin['id']}/checkout", json={
        "appointment_id": checkin["id"]
    })
    assert res.status_code == 200

	
def test_dashboard_count(client):
    site = client.post("/api/sites",json ={
        "name":"test_rama",
        "address":"Vijayawada"
    }).get_json()
    client.post(f"/api/sites/{site['id']}/spots", json={
        "spot_label": "A1"
    })
    trailer = client.post("/api/trailers",json ={
        "trailer_type":"REEFER",
        "trailer_number" : "1234",
        "carrier_name":"ABC"
    }).get_json()

    checkin = client.post("/appointments/checkin", json={
        "site_id": site["id"],
        "trailer_id": trailer["id"]
    }).get_json()

    res = client.get(f"/api/dashboard/{site['id']}")
    data = res.get_json()
    assert data["trailer_count"] == 1