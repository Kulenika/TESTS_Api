from utils.assertions import Assert
from http import HTTPStatus
from api.questions_api import api
def test_registration():
    email = 'eve.holt@reqres.in'
    password = 'language8'
    resp = api.registration(email, password)
    assert resp.status_code == HTTPStatus.OK
    Assert.validate_schema(resp.json())

def test_uncorrect_registration():
    email = 'eve.holt@reqres.in'
    res = api.uncorrect_registration()
    res_body = res.json()
    resp = api.uncorrect_registration(email)
    assert resp.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(resp.json())
    Assert.validate_schema(res_body)
    assert res_body['data']['email'] == 'eve.holt@reqres.in'
    example = {
        "data": {
            'error':'Missing password'
        }
    }

    assert example == res_body