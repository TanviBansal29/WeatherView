from unittest import mock
from unittest.mock import MagicMock
from unittest import TestCase
from config.config import Config

from db.database import Database
from helpers.exceptions import DbException

class TestAccount(TestCase):

    def setUp(self):
        self.obj=Database(Config.DATABASE_NAME)
        self.obj.cursor = mock.Mock()
        self.obj.connection = mock.Mock()

    def test_add_item(self):
        self.obj.cursor.lastrowid = 2
        response = self.obj.add_item('',"")
        self.obj.cursor.execute.assert_called_once()
        self.assertEqual(response, 2)

    def test_add_item_failure(self):
        self.obj.cursor.execute.side_effect = DbException()
        with self.assertRaises(DbException):
            self.obj.add_item('',"")
      

    def test_get_item(self):
        self.obj.cursor.fetchone.return_value = [("",)]
        response = self.obj.get_item('',())
        self.obj.cursor.execute.assert_called_once()
        self.assertEqual(response, [("",)])

    def test_get_item_failure(self):
        self.obj.cursor.execute.side_effect = DbException()
        with self.assertRaises(DbException):
            self.obj.get_item('',"")

    def test_get_items(self):
        self.obj.cursor.fetchall.return_value = [("",),("",)]
        response = self.obj.get_items("",())
        self.obj.cursor.execute.assert_called_once()
        self.assertEqual(response, [("",),("",)])

    def test_get_items_failure(self):
        self.obj.cursor.execute.side_effect = DbException()
        with self.assertRaises(DbException):
            self.obj.get_items('',"")

    







