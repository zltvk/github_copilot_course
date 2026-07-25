from fastapi.testclient import TestClient

from src.app import app


def test_can_unregister_participant_from_activity():
    # Arrange
    client = TestClient(app)
    email = "new.student@mergington.edu"
    initial_activities = client.get("/activities").json()

    assert email not in initial_activities["Chess Club"]["participants"]

    # Act
    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    activities_after_signup = client.get("/activities").json()
    unregister_response = client.delete(f"/activities/Chess Club/participants/{email}")
    activities_after_unregister = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert email in activities_after_signup["Chess Club"]["participants"]
    assert unregister_response.status_code == 200
    assert email not in activities_after_unregister["Chess Club"]["participants"]
