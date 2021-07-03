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
RANGE_NAME = 'Users!A1:B'

def google_account():
    creds = service_account.Credentials.from_service_account_file('google_searvice_account.json', scopes=SCOPES)#Credentials.from_authorized_user_file('google_searvice_account.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return {
        'res':values
    }

if __name__ == '__main__':
    google_account()