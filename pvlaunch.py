import tkinter, os

launch = tkinter.Tk()

def install_libs():
    os.system("pip install gspread")
    os.system("pip3 install gspread")
    os.system("python -m pip install gspread")
    os.system("pip3.10 install oauth2client")
    os.system("pip install oauth2client")
    os.system("pip3 install oauth2client")
    os.system("python -m pip install oauth2client")

def cd():
    return f"{os.path.dirname(__file__)}"

tkinter.Button(launch, text="Play Game", command=lambda:(os.system(f"python {cd()}\\tk_play_game.py"))).pack()

tkinter.Button(launch, text="Result Game", command=lambda:(cd(),os.system(f"python {cd()}\\tk_result_game.py"))).pack()

tkinter.Button(launch, text="Create Game", command=lambda:(cd(),os.system(f"python {cd()}\\tk_create_game.py"))).pack()

tkinter.Button(launch, text="Install Libs", command=lambda:install_libs()).pack()

tkinter.Button(launch, text="Quit", command=lambda:launch.destroy()).pack()



tkinter.mainloop()
