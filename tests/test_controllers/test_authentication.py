from unittest import mock
from unittest import TestCase
from handler.authentication import Authentication

class TestAccount(TestCase):
    def setUp(self):
        self.obj = Authentication("tanvi", "Tanvi12@", "delhi", "121212")

    @mock.patch("controllers.authentication.db")
    def test_get_role_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = ("user", "VX23a")
        response = self.obj.get_role()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, {'role': 'VX23a', 'user_id': 'user'})

    @mock.patch("controllers.authentication.db")
    def test_get_role_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = None
        response = self.obj.get_role()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("controllers.authentication.db")
    def test_verify_user_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = ("tanvi")
        response = self.obj.verify_user()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, True)

    @mock.patch("controllers.authentication.db")
    def test_verify_user_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = None
        response = self.obj.verify_user()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, False)

    @mock.patch("controllers.authentication.db")
    def test_verify_username_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = ("tanvi")
        response = self.obj.verify_username()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, False)

    @mock.patch("controllers.authentication.db")
    def test_verify_username_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = None
        response = self.obj.verify_username()
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, True)

    @mock.patch("controllers.authentication.db")
    def test_create_account_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 54
        response = self.obj.create_account()
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, 54)

    @mock.patch("controllers.authentication.db")
    def test_create_account_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = None
        response = self.obj.create_account()
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, None)
