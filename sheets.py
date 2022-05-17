import gspread, os
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file" , "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(f"{os.path.dirname(__file__)}\\creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("BddBAC").sheet1

data = sheet.get_all_records()


print(data)

for dictionary in data:
    for key in dictionary.keys():
        print(dictionary[key])
        
        
def delete_sheet(sheet):
    print(len(data))
    for row in range(len(data)+1):
        sheet.delete_rows(1)
    
delete_sheet(sheet)