from unittest import mock
from unittest import TestCase
from business.history import History


class TestAccount(TestCase):
    def setUp(self):
        self.obj = History("vx12a", "delhi")

    @mock.patch("controllers.history.db")
    def test_view_history_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [("datetime", "currentweather", "cityname", "delhi")]
        response = self.obj.view_history()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, [("datetime", "currentweather", "cityname", "delhi")])

    @mock.patch("controllers.history.db")
    def test_view_history_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = None
        response = self.obj.view_history()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("controllers.history.db")
    def test_insert_history_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 21
        response = self.obj.insert_history()
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, 21)

    @mock.patch("controllers.history.db")
    def test_insert_history_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = None
        response = self.obj.insert_history()
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, None)
