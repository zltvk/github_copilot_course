from fastapi.testclient import TestClient

from src.app import app


def test_can_unregister_participant_from_activity():
    client = TestClient(app)
    email = "new.student@mergington.edu"

    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert signup_response.status_code == 200

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]

    unregister_response = client.delete(f"/activities/Chess Club/participants/{email}")
    assert unregister_response.status_code == 200

    updated_activities = client.get("/activities").json()
    assert email not in updated_activities["Chess Club"]["participants"]
