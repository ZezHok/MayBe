import requests
import json
from services import auth


def screen():
    headers = {"cookie": auth.establish()}
    r = requests.get("http://vkusomania-backend.qtelecom.ru/v9/feed_units/main_screen", headers=headers)
    fid_unit = json.loads(r.text)['data']['feed_unit_list']
    skin_list = []
    for i in range(len(fid_unit)):
        skin_list.append(fid_unit[i]['skin'])
    return skin_list
