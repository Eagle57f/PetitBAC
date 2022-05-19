import random
import tkinter, sheets

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
    first_row = [random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])]
    print(first_row)
    first_row = first_row + all_cat
    sheets.set_first_row(first_row)


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

print(first_row)