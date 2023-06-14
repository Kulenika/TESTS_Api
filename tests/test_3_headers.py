import re
from utils.assertions import Assert

from api.httpbin import http_bin_api
from http import HTTPStatus

def test_list_html():
    resp = http_bin_api.list_html()
    assert resp.status_code == HTTPStatus.OK
    assert resp.headers['Content-Type'] == 'text/html; charset=utf-8'

def test_robots():
    resp = http_bin_api.robots()

    assert resp.status_code == HTTPStatus.OK
    assert resp.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', resp.text, flags=re.DOTALL )


def test_ip():
    resp = http_bin_api.ip()
    assert resp.status_code == HTTPStatus.OK
    if resp.headers['Content-Type'] == 'application/json':
        Assert.validate_schema(resp.json())
        origin = resp.json()['origin']
        assert re.fullmatch(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.', origin)
