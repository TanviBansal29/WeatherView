from unittest import mock
from unittest import TestCase
from api_handler.api_client import ApiClient


class TestApiClient(TestCase):
    def setUp(self):
        self.obj = ApiClient()

    @mock.patch("requests.get")
    def test_get_data_by_city_success(self, mock_requests_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "cloud_pct": 20,
            "temp": 24,
            "feels_like": 24,
            "humidity": 53,
            "min_temp": 24,
            "max_temp": 24,
            "wind_speed": 2.06,
            "wind_degrees": 120,
            "sunrise": 1701221083,
            "sunset": 1701258847,
        }
        mock_requests_get.return_value = mock_response

        response = self.obj.get_data_by_city({})
        mock_requests_get.assert_called_once()
        self.assertEqual(response, [24, 24, 2.06, "06:54:43 A.M.", "17:24:07 P.M."])

    @mock.patch("requests.get")
    def test_get_data_by_city_failure(self, mock_requests_get):
        mock_response = mock.Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {}
        mock_requests_get.return_value = mock_response

        response = self.obj.get_data_by_city({})
        mock_requests_get.assert_called_once()
        self.assertEqual(response, None)

    @mock.patch("requests.get")
    def test_forecast_info_success(self, mock_requests_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
    "forecast": {
        "forecastday": [
            {
                "date": "2023-11-29",
                "day": {
                    "maxtemp_c": 25.7,
                    "mintemp_c": 17.9,
                    "maxwind_mph": 4.5,
                },
                "astro": {
                    "sunrise": "06:54 AM",
                    "sunset": "05:24 PM",
                }
            },
        ]
    },
}
        mock_requests_get.return_value = mock_response
        response = self.obj.forecast_info({})
        mock_requests_get.assert_called_once()
        self.assertEqual(
            response,
            [
                ['2023-11-29', 25.7, 17.9, 4.5, '06:54 AM', '05:24 PM']
            ],
        )

    @mock.patch("requests.get")
    def test_forecast_info_failure(self, mock_requests_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_requests_get.return_value = mock_response
        response = self.obj.get_data_by_city({})
        mock_requests_get.assert_called_once()
        self.assertEqual(response, None)

