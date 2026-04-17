from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset the in-memory activities store for every test."""
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))

    yield

    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app)
