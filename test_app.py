import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello, World!')
        
        from app import app

def test_hello_world():
    tester = app.test_client()
    response = tester.get('/')
    assert response.data == b'Hello, World!'