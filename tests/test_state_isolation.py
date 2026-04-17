def test_unregister_then_signup_again_succeeds(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    unregister_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert unregister_response.status_code == 200
    assert signup_response.status_code == 200
    assert email in participants


def test_repeated_unregister_returns_not_found(client):
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"

    # Act
    first_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    second_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    second_payload = second_response.json()

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 404
    assert second_payload["detail"] == "Participant not found in this activity"


def test_test_state_starts_from_known_seed_data(client):
    # Arrange
    activity_name = "Gym Class"
    seeded_email = "john@mergington.edu"

    # Act
    response = client.get("/activities")
    participants = response.json()[activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert seeded_email in participants
