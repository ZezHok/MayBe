#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from test_skin_list import test_skin_list

CREDENTIALS_FILE = '/Users/j.chistova/PycharmProjects/MayBe/AB Julia-3b2801f7c8f6.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

spreadsheet = 'https://docs.google.com/spreadsheets/d/1KLCHgvUbsRyBbmd8f5jR4Zv3qrRaSTymKiBLhvLGDY0/edit?usp=sharing'
spreadsheet_id = '1KLCHgvUbsRyBbmd8f5jR4Zv3qrRaSTymKiBLhvLGDY0'

skin_list = test_skin_list()
for i in range(len(skin_list)):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Num!A%s" % str(i+1),
             "majorDimension": "COLUMNS",
             "values": [[skin_list[i]]]},
        ]
    }).execute()

print(results)
