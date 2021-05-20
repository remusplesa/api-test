from api.utils import get_ip_info
from api.utils import parse_response


class TestGetIpInfo:
    def test_ok_ip(self):
        response, errors = get_ip_info("84.137.201.100")

        assert len(errors) == 0
        assert response == {
            "country": "Germany",
            "country_code": "DE",
            "region": "BW",
            "city": "Ulm",
            "latitude": 48.3991,
            "longitude": 9.9717
        }

    def test_bad_ip_err(self):
        response, errors = get_ip_info("0")

        assert response is None
        assert errors == [
            {
                "ip_value_error": "0 is not a valid address"
            }
        ]

    def test_bad_url(self):
        response, errors = get_ip_info(
            "84.137.201.100", "http://ip_api.co/json")
        assert response is None
        assert errors[0]["request_exception"] is not None


class TestParseResponse:
    response_in_ok = {
        "status": "success",
        "country": "Germany",
        "countryCode": "DE",
        "region": "BW",
        "regionName": "Baden-Württemberg",
        "city": "Ulm",
        "zip": "89077",
        "lat": 48.3991,
        "lon": 9.9717,
        "timezone": "Europe/Berlin",
        "isp": "Deutsche Telekom AG",
        "org": "Deutsche Telekom AG",
        "as": "AS3320 Deutsche Telekom AG",
        "query": "84.137.201.100"
    }

    response_out_ok = {
        "country": "Germany",
        "country_code": "DE",
        "region": "BW",
        "city": "Ulm",
        "latitude": 48.3991,
        "longitude": 9.9717
    }

    response_in_bad = {
        "countryCode": "DE",
        "region": "BW",
        "regionName": "Baden-Württemberg",
        "city": "Ulm",
        "zip": "89077",
        "lat": 48.3991,
        "lon": 9.9717,
        "timezone": "Europe/Berlin",
        "isp": "Deutsche Telekom AG",
        "org": "Deutsche Telekom AG",
        "as": "AS3320 Deutsche Telekom AG",
        "query": "84.137.201.100"
    }

    def test_response_ok(self):
        errors = []
        parsed_response = parse_response(self.response_in_ok, errors)

        assert len(errors) == 0
        assert parsed_response.dict() == self.response_out_ok

    def test_response_err(self):
        errors = []
        parsed_response = parse_response(self.response_in_bad, errors)

        assert parsed_response is None
        assert len(errors) == 1
        assert errors == [
            {'KeyError': "'country' not in dict_keys(['country', 'country_code', 'region', ""'city', 'latitude', 'longitude'])"}
        ]
