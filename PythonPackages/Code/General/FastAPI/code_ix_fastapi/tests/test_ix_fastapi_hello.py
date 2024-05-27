from unittest import TestCase
from starlette.testclient import TestClient
from ix_fastapi_hello import app

client = TestClient(app)

class TestFastApi(TestCase):
    def test_hello(self):
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.json() == {"hello": "world"}
        assert response.json() != {"hello": "WORLD"}
