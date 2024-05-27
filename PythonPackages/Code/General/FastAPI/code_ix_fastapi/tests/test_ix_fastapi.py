from unittest import TestCase
from starlette.testclient import TestClient
from ix_fastapi import app

client = TestClient(app)


class TestFastApi(TestCase):
    def test_01_read_item(self):
        response = client.get("/item/1")
        assert response.status_code == 200
        assert response.json() == {'item_id': 1, 'name': 'Bar'}

    def test_02_read_item_negative(self):
        response = client.get("/item/Bar")
        assert response.status_code == 422
        assert response.json() != {'item_id': 1, 'name': 'Bar'}
        assert response.json() == {'detail': [{'loc': ['path', 'item_id'], 'msg': 'value is not a valid integer',
                                               'type': 'type_error.integer'}]}

    def test_03_read_items(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [{'item_id': 1, 'name': 'Bar'},
                                   {'item_id': 2, 'name': 'Baz'}]

    def test_04_post_item(self):
        response = client.post("/item/3/Foo")
        assert response.status_code == 200
        assert response.json() == {'item_id': 3, 'name': 'Foo'}

    def test_05_post_item_negative_already_existing(self):
        response = client.post("/item/3/Foo")
        assert response.status_code == 405
        assert response.json() == {"detail": "item with item_id 3 already exists"}

    def test_06_post_item_negative_typo(self):
        response = client.post("/item/Baz/42")
        assert response.status_code == 422
        assert response.json() != {'item_id': 3, 'name': 'Foo'}
        assert response.json() == {'detail': [{'loc': ['path', 'item_id'], 'msg': 'value is not a valid integer',
                                              'type': 'type_error.integer'}]}

    def test_07_read_items_after_post(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [{'item_id': 1, 'name': 'Bar'},
                                   {'item_id': 2, 'name': 'Baz'},
                                   {'item_id': 3, 'name': 'Foo'}]

    def test_08_put_item(self):
        response = client.put("/item/3/Wow")
        assert response.status_code == 200
        assert response.json() == {'item_id': 3, 'name': 'Wow'}

    def test_09_put_item_negative(self):
        response = client.put("/item/4/Wow")
        assert response.status_code == 406
        assert response.json() == {'detail': 'item with item_id 4 not found'}

    def test_10_read_items_after_put(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [{'item_id': 1, 'name': 'Bar'},
                                   {'item_id': 2, 'name': 'Baz'},
                                   {'item_id': 3, 'name': 'Wow'}]

    def test_11_delete_item(self):
        response = client.delete("/item/3")
        assert response.status_code == 200
        assert response.json() == {'message': 'item with item_id 3 deleted from items'}

    def test_12_delete_item_negative(self):
        response = client.delete("/item/4")
        assert response.status_code == 406
        assert response.json() == {'detail': 'item with item_id 4 not found'}

    def test_13_read_items_after_put(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [{'item_id': 1, 'name': 'Bar'},
                                   {'item_id': 2, 'name': 'Baz'}]
