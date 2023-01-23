from rest_framework.test import APIClient
import pytest

client = APIClient()

@pytest.mark.django_db
def test_get_songs(songs):
    response = client.get('/api/songs')
    assert response.status_code == 200