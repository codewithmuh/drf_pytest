from pytest_factoryboy import register
from .factories import SongFactory
import pytest

# Register Approach

register(SongFactory)

# pytest.fixture() Approach

@pytest.fixture
def songs():
    return SongFactory.create_batch(10)