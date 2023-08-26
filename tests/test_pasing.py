import requests
import tests.test_data as test_data


def test_input_parsing():
    rq_body = test_data.input
    response = requests.post("http://localhost:5000/parser", json=rq_body)
    assert response.status_code == 200
    assert response.json() == test_data.output
