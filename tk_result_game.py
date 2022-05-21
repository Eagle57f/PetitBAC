import tkinter, gspread, os
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file" ,
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(f"{os.path.dirname(__file__)}\\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("BddBAC").sheet1
data = sheet.get_all_values()


   
total_rows = len(data) 
total_columns = len(data[0]) 

root = tkinter.Tk() 
      
for i in range(total_rows): 
    for j in range(total_columns): 
            
        entry = tkinter.Entry(root, width=20, font=('Arial',12))
            
        entry.grid(row=i, column=j) 
        entry.insert('end', data[i][j]) 
        entry.config(state='readonly')
  


root.mainloop() 