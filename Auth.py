#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = '/Users/j.chistova/PycharmProjects/MayBe/AB Julia-3b2801f7c8f6.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

spreadsheet = 'https://docs.google.com/spreadsheets/d/1KLCHgvUbsRyBbmd8f5jR4Zv3qrRaSTymKiBLhvLGDY0/edit?usp=sharing'
spreadsheet_id = '1KLCHgvUbsRyBbmd8f5jR4Zv3qrRaSTymKiBLhvLGDY0'

batch_update_values_request_body = {
    # How the input data should be interpreted.
    'value_input_option': 'USER_ENTERED',  # TODO: Update placeholder value.

    # The new values to apply to the spreadsheet.
    'data': [
        {"range": "Num!B2:C3",
         "majorDimension": "ROWS", # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": [["This is B2", "This is C2"], ["This is B3", "This is C3"]]},

        {"range": "Num!D5:E6",
         "majorDimension": "COLUMNS", # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
         "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}],
}

request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id,
                                                      body=batch_update_values_request_body)
response = request.execute()

print(response)
