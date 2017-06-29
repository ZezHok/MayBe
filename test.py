import requests
import json


def test_registration():
    data = {"device_info": {"os": "ios", "model": "iPhone 6s Plus", "os_version": "9.3.5", "build_number": 142,
                            "screen_width": 1242},
            "phone_number": "73330001100"}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration", json=data)
    cookie = r.headers['Set-Cookie'].split(';')
    return cookie[0]


def test_confirm():
    headers = {"cookie": test_registration()}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration/confirm", json={"code": "1111"},
                      headers=headers)
    token = json.loads(r.text)['data']['token']
    return token


def test_establish():
    data = {"token": test_confirm(),
            "device_info": {
                "os": "ios",
                "model": "iPhone 6s Plus",
                "os_version": "9.3.5",
                "build_number": 142,
                "screen_width": 1242
            }
            }
    headers = {"cookie": test_registration()}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/sessions/establish", json=data, headers=headers)
    cookie = r.headers['Set-Cookie'].split(';')
    return cookie[0]

def test_main_screen():
    headers = {"cookie": test_establish()}
    r = requests.get("http://vkusomania-backend.qtelecom.ru/v9/feed_units/main_screen", headers=headers)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    fid_unit = json.loads(r.text)['data']['feed_unit_list']
    #a = fid_unit['data']['feed_unit_list']
    for i in range(len(fid_unit)):
        print(fid_unit[i]['skin'])
