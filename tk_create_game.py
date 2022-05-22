import random, tkinter, gspread, os
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(f"{os.path.dirname(__file__)}\\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("BddBAC").sheet1
data = sheet.get_all_records()

all_cat = []
new_cat = ""
str_all_cats = ""
menu = tkinter.Tk()
new_cat = tkinter.StringVar(menu)
menu.geometry("400x250")

def add_cat(t):
    global label, str_all_cats
    if t != "" and t != " ":
        all_cat.append(t)

        str_all_cats = str_all_cats + " " + t
        label.configure(text=f"Les cats: {str_all_cats}")

def delete_all_cats():
    global str_all_cats
    all_cat.clear()
    str_all_cats = ""
    label.configure(text=f"Les cats: {str_all_cats}")

def save():
    global first_row
    first_row = [random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u"])]
    print(first_row)
    first_row = first_row + all_cat
    for row in range(len(data)+1):
        sheet.delete_rows(1)
    sheet.insert_row(first_row, 1)
    
def get_sheet_letter():
    i = 0
    for key in data[0].keys():
        if i == 0:
            letter_and_code = key
        i += 1
    list_letter_and_code = letter_and_code.split(":")
    return list_letter_and_code


label = tkinter.Label(menu, text=str_all_cats)
label.pack()

entry = tkinter.Entry(menu, width=30, bg="lightblue", fg="black", textvariable="Les cats:")
entry.pack()



add_cat_button = tkinter.Button(menu, text="Add Category", command=lambda:(add_cat(entry.get()), entry.delete(0, tkinter.END)))
add_cat_button.pack()


delete_all_cats_button = tkinter.Button(menu, text="Delete All Cats", command=lambda:(delete_all_cats()))
delete_all_cats_button.pack()

save_exit_button = tkinter.Button(menu, text="Save and Exit", command=lambda:(save(), menu.destroy()))
save_exit_button.pack()

tkinter.mainloop()