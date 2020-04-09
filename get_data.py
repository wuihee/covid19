from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Allows read-only access to the user's sheets and their properties.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

spread_sheet_ID = '13_YuaT2t51h-fKzTCOqEvgLRBIkzKqtbFZTPmAqbzW4'
spread_sheet_range = 'W4:X131'


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spread_sheet_ID, range=spread_sheet_range).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        return values


if __name__ == '__main__':
    main()
