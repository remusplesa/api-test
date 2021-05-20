import requests
import ipaddress
from schemas.schema import SessionLocationDetails


API_URL = "http://ip-api.com/json"


def parse_response(response, errors):
    try:
        return SessionLocationDetails(
            country=response["country"],
            country_code=response["countryCode"],
            region=response["region"],
            city=response["city"],
            latitude=response["lat"],
            longitude=response["lon"]
        )
    except KeyError as err:
        available_options = SessionLocationDetails.schema()[
            'properties'].keys()
        errors.append(
            {"KeyError": f"{err} not in {available_options}"})


def get_ip_info(ip, address=API_URL):
    parsed_response = None
    errors = []

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        errors.append({"ip_value_error": f"{ip} is not a valid address"})
        return parsed_response, errors

    try:
        response = requests.get(f"{address}/{ip}").json()
    except requests.exceptions.RequestException as err:
        errors.append({"request_exception": str(err)})
        return parsed_response, errors

    parsed_response = parse_response(response, errors)

    return parsed_response, errors
