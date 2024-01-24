from unittest import mock
from unittest import TestCase
from src.handler.weather import Weather


class TestAccount(TestCase):
    def setUp(self):
        self.obj = Weather("delhi", "51", "21")

    @mock.patch("api_handler.api_client.ApiClient.get_data_by_city")
    def test_get_weather_by_city_success(self, mocked_db_object):
        mocked_db_object.return_value = ("weather_data")
        response = self.obj.get_weather_by_city()
        mocked_db_object.assert_called_once()
        self.assertEqual(response, ( "weather_data"))

    @mock.patch("api_handler.api_client.ApiClient.get_data_by_city")
    def test_get_weather_by_city_failure(self, mocked_db_object):
        mocked_db_object.return_value = None
        response = self.obj.get_weather_by_city()
        mocked_db_object.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("api_handler.api_client.ApiClient.get_data_by_city")
    def test_get_weather_by_coordinates_success(self, mocked_db_object):
        mocked_db_object.return_value = ("weather_data")
        response = self.obj.get_weather_by_coordinates()
        mocked_db_object.assert_called_once()
        self.assertEqual(response, ( "weather_data"))

    @mock.patch("api_handler.api_client.ApiClient.get_data_by_city")
    def test_get_weather_by_coordinates_failure(self, mocked_db_object):
        mocked_db_object.return_value = None
        response = self.obj.get_weather_by_coordinates()
        mocked_db_object.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("api_handler.api_client.ApiClient.forecast_info")
    def test_get_forecast_success(self, mocked_db_object):
        mocked_db_object.return_value = ("weather_data")
        response = self.obj.get_forecast(days=2)
        mocked_db_object.assert_called_once()
        self.assertEqual(response, ( "weather_data"))

    @mock.patch("api_handler.api_client.ApiClient.forecast_info")
    def test_get_forecast_failure(self, mocked_db_object):
        mocked_db_object.return_value = None
        response = self.obj.get_forecast(days=2)
        mocked_db_object.assert_called_once()
        self.assertEqual(response, None)