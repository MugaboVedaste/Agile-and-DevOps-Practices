
def test_status_page_reports_healthy_database(client):
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["database"] == "connected"
