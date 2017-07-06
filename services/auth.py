import requests
import json


def registration():
    data = {"device_info": {"os": "ios", "model": "iPhone 6s Plus", "os_version": "9.2", "build_number": 142,
                            "screen_width": 1242}, "phone_number": "+73330001117"} # значение phone_number нужно каждый раз заменять
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration", json=data)
    cookie = r.headers['Set-Cookie'].split(';')
    return cookie[0]

def confirm():
    headers = {"cookie": registration()}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration/confirm", json={"code": "1111"},
                      headers=headers)
    token = json.loads(r.text)['data']['token']
    return token


def establish():
    data = {"token": confirm(),
            "device_info": {
                "os": "ios",
                "model": "iPhone 6s Plus",
                "os_version": "9.3.5",
                "build_number": 142,
                "screen_width": 1242
            }
            }
    headers = {"cookie": registration()}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/sessions/establish", json=data, headers=headers)
    cookie = r.headers['Set-Cookie'].split(';')
    return cookie[0]
