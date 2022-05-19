import gspread, os
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file" , "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(f"{os.path.dirname(__file__)}\\creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("BddBAC").sheet1

data = sheet.get_all_records()



def get_sheet_letter():
    i = 0
    for key in data[0].keys():
        if i == 0:
            letter_and_code = key
        i += 1
    list_letter_and_code = letter_and_code.split(":")
    return list_letter_and_code
        

def set_first_row(first_row):
    for row in range(len(data)+1):
        sheet.delete_rows(1)
    sheet.insert_row(first_row, 1)