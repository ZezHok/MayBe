import requests
import json


def registration(tel):
    data = {"device_info": {"os": "ios", "model": "iPhone 6s Plus", "os_version": "9.2", "build_number": 142,
                            "screen_width": 1242}, "phone_number": tel}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration", json=data)
    cookie = r.headers['Set-Cookie'].split(';')
    print r.url
    return cookie[0]

def confirm(telf):
    headers = {"cookie": registration(tel=telf)}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration/confirm", json={"code": "1111"},
                      headers=headers)
    token = json.loads(r.text)['data']['token']
    print r.url
    return token


def establish(telm):
    data = {"token": confirm(telf=telm),
            "device_info": {
                "os": "ios",
                "model": "iPhone 6s Plus",
                "os_version": "9.3.5",
                "build_number": 142,
                "screen_width": 1242
            }
            }
    headers = {"cookie": registration(tel=telm)}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/sessions/establish", json=data, headers=headers)
    cookie = r.headers['Set-Cookie'].split(';')
    print r.url
    return cookie[0]
