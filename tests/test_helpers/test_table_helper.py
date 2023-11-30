from unittest import mock
from unittest import TestCase

from helpers.table_helper import TableHelper


class TestTableHelper(TestCase):
    def setUp(self):
        self.obj = TableHelper()

    @mock.patch("helpers.table_helper.tb")
    def test_print_table_username(self,mock_tabulate):
        mock_tabulate.return_value = "tanvi"
        response = self.obj.print_table({}, "username")
        mock_tabulate.assert_called_once()
        self.assertEqual(response, None)
        
    @mock.patch("helpers.table_helper.tb")
    def test_print_table_city(self,mock_tabulate):
        mock_tabulate.return_value = "tanvi"
        response = self.obj.print_table({}, "city")
        mock_tabulate.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("helpers.table_helper.tb")
    def test_print_table_history(self,mock_tabulate):
        mock_tabulate.return_value = "tanvi"
        response = self.obj.print_table({}, "history")
        mock_tabulate.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("helpers.table_helper.tb")
    def test_print_table_weather(self,mock_tabulate):
        mock_tabulate.return_value = "tanvi"
        response = self.obj.print_table({}, "weather")
        mock_tabulate.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("helpers.table_helper.tb")
    def test_print_table_forecast(self,mock_tabulate):
        mock_tabulate.return_value = "tanvi"
        response = self.obj.print_table({}, "forecast")
        mock_tabulate.assert_called_once()
        self.assertEqual(response, None)
              
        