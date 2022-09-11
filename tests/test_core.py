from app.core import make_post
from app.models import Item

from tests.config import TestingSessionLocal


def test_core_make_post():
    data = {
        "name": "687435AAD0F6497188D532DD9E0E005C",
        "status": True
    }
    result = make_post(model=Item, data=data, db=TestingSessionLocal)

    assert data['name'] == result['name']
    assert data['status'] == result['status']
