import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
# from dotenv import load_dotenv
# from pathlib import Path

# dotenv_path = Path('.env')
# load_dotenv(dotenv_path=dotenv_path)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SHEET_ID = '1WCW3nC3Xv8JU7HKGmYpIq5AwS2qBb5DSMfXSKh6YcMw'
#RANGE_NAME = 'Users!A1:B'

def google_account(RANGE_NAME='Users!A1:B'):
    creds = service_account.Credentials.from_service_account_file('google_searvice_account.json', scopes=SCOPES)#Credentials.from_authorized_user_file('google_searvice_account.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return {
        'res':values
    }

def get_all_posts(RANGE_NAME='Posts!A1:H'):
    creds = service_account.Credentials.from_service_account_file('google_searvice_account.json', scopes=SCOPES)#Credentials.from_authorized_user_file('google_searvice_account.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return {
        'data':values
    }

def search_posts(bf_industry_id, af_industry_id, RANGE_NAME='Posts!A1:H'):
    creds = service_account.Credentials.from_service_account_file('google_searvice_account.json', scopes=SCOPES)#Credentials.from_authorized_user_file('google_searvice_account.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    res = []

    if bf_industry_id and af_industry_id:
        for i in values:
            if i[2] == f"{bf_industry_id}" and i[3] == f"{af_industry_id}":
                res.append(i)

        return {
            'data':res
        }
    elif bf_industry_id:
        for i in values:
            if i[2] == f"{bf_industry_id}":
                res.append(i)

        return {
            'data':res
        }
    elif af_industry_id:
        for i in values:
            if i[3] == f"{af_industry_id}":
                res.append(i)

        return {
            'data':res
        }
    else:
        return {
            'data': res
        }

if __name__ == '__main__':
    google_account()