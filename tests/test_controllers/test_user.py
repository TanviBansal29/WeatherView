from unittest import mock
from unittest import TestCase
from controllers.user import User


class TestAccount(TestCase):
    def setUp(self):
        self.obj = User("tanvi", "delhi")

    @mock.patch("controllers.user.db")
    def test_fetch_user_data_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = ("user_data",)
        response = self.obj.fetch_user_data()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, ("user_data",))

    @mock.patch("controllers.user.db")
    def test_fetch_user_data_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = None
        response = self.obj.fetch_user_data()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, None)

        ###################
    @mock.patch("controllers.user.db")
    def test_fetch_user_by_city_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = ("user_data",)
        response = self.obj.fetch_user_by_city()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, ("user_data",))

    @mock.patch("controllers.user.db")
    def test_fetch_user_by_city_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = None
        response = self.obj.fetch_user_by_city()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, None)

        #############
    # @mock.patch("controllers.user.db")
    # def test_fetch_user_data_success(self, mocked_db_object):
    #     mocked_db_object.get_items.return_value = ("user_data",)
    #     response = self.obj.fetch_user_data()
    #     mocked_db_object.get_items.assert_called_once()
    #     self.assertEqual(response, ("user_data",))

    # @mock.patch("controllers.user.db")
    # def test_fetch_user_data_failure(self, mocked_db_object):
    #     mocked_db_object.get_items.return_value = None
    #     response = self.obj.fetch_user_data()
    #     mocked_db_object.get_items.assert_called_once()
    #     self.assertEqual(response, None)