import tkinter, gspread, os
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import messagebox


scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file" ,
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(f"{os.path.dirname(__file__)}\\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("BddBAC").sheet1
cats_and_letter = sheet.get_all_values()[0]


letter = cats_and_letter[0]
cats = cats_and_letter[1:]

count_cats = 0
list_of_entry = []
name = ""


def save():
    list_of_response = [name_entry.get()]
    for entrys in list_of_entry:
        list_of_response.append(entrys.get())
    sheet.insert_row(list_of_response, 2)
    
def save_and_exit():
    if name_entry.get() != "" and name_entry.get() != " ":
        save()
        game.destroy()
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer un nom")



game = tkinter.Tk()
game.geometry("630x300")


letter_label = tkinter.Label(game, text=f"La lettre pour cette partie est: {letter}")
letter_label.grid(row=1, column=0)

save_button = tkinter.Button(game, text="Save and Exit", command=lambda:(save_and_exit()))
save_button.grid(row=0, column=2)

name_label = tkinter.Label(game, text="Nom:")
name_label.grid(row=0, column=0)

name_entry = tkinter.Entry(game, width=40, bg="lightblue", fg="black")
name_entry.grid(row=0, column=1)

for item in cats:
    count_cats += 1
    tkinter.Label(game, text=item).grid(row=count_cats+1, column=0)
    entry = tkinter.Entry(game, width=60, bg="lightblue", fg="black")
    entry.grid(row=count_cats+1, column=1)
    list_of_entry.append(entry)
print(list_of_entry)



game.mainloop()