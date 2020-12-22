import requests


def test_put_request_with_unvalid_data():
    BASE = "http://127.0.0.1:5000/"

    response = requests.put(BASE + 'Review', {})
    print(response.json())
