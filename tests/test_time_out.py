from api.httpbin import http_bin_api
from http import HTTPStatus

def test_time_out():
    resp = http_bin_api.time_out(2)
    assert not resp[0]

