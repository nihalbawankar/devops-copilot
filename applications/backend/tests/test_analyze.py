from .conftest import client


def test_analyze():
    response = client.get("/analyze")

    assert response.status_code == 501

    body = response.json()

    assert body["success"] is False
    assert body["error"]["message"] == "Analyze service not implemented yet"
