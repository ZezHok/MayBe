from test_skin_list import test_skin_list

import requests
import json


def test():
    number="73330001117"
    data = {"device_info": {"os": "ios", "model": "iPhone 6s Plus", "os_version": "9.3.5", "build_number": 142,
                            "screen_width": 1242},
            "phone_number": "73330001100"}
    r = requests.post("http://vkusomania-backend.qtelecom.ru/v9/accounts/registration", json=data)
    cookie = r.headers['Set-Cookie'].split(';')
    print("!!!!!!")
    print cookie[0]