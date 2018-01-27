import unittest

from app import Todo
from app import app


class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        todos = Todo.objects.all()
        for todo in todos:
            todo.delete()

    def test_index(self):
        rv = self.app.get('/')
        assert "Todo" in rv.data

    def test_todo(self):
        self.app.post('/add', data = dict(content="testtodo"))
        todo = Todo.objects.get_or_404(content="testtodo")
        assert todo is not None