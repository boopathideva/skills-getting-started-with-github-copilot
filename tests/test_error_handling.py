def test_signup_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Activity not found"


def test_signup_duplicate_participant_returns_bad_request(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": existing_email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload["detail"] == "Student already signed up"


def test_unregister_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_not_found(client):
    # Arrange
    activity_name = "Art Studio"
    email = "missing@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Participant not found in this activity"


def test_signup_missing_email_returns_validation_error(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup")
    payload = response.json()

    # Assert
    assert response.status_code == 422
    assert payload["detail"][0]["loc"][-1] == "email"
