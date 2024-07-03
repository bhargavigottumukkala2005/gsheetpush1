import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds=ServiceAccountCredentials.from_json_keyfile_name('gsheetautomation/gsheet-426913-6e02a0c69199.json')

client=gspread.authorize(creds)

sheet=client.open('gsheet_push').sheet1

sentence= 'This is a test code'

sheet.append_row([sentence])

print('Sentence successfully pushed to the gsheet')

