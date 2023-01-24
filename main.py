import re
from tkinter import *
from tkinter import ttk
import hashlib
from tkinter import messagebox
import json

#My sized fonts
DEFAULT_FONT_STYLE = ("Arial", 14)

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Def of my functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def check(mdp):  
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*"]
    lower = 0
    alpha = 0
    chiffre = 0
    special = 0
    len_mdp = len(mdp)

    for letter in mdp:
        if letter.isalpha():
            alpha += 1
        if letter.islower():
            lower += 1
        if letter in special_char:
            special += 1
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            chiffre += 1

    if lower != 0 and alpha != 0 and chiffre != 0 and special != 0 and len_mdp > 7:
        correct = 1
        return correct
    else:
        correct = 0
        return 

    # match letter:
    #     case letter.isalpha():
    #         alpha += 1

    #     case letter.islower():
    #         lower += 1

    #     case letter in special_char:
    #         special += 1
        
    #     case letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    #         chiffre += 1


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI general and notebook ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

gui = Tk()
gui.title("Passwords Manager")
gui.geometry("400x400")
gui.resizable(False, False)

# with open('password.json', 'r') as f:
#     password_list = json.load(f)

pages = ttk.Notebook(gui)
pages.pack()

#Create my 2 MAIN Frame
# CreatePassword Frame
create_password_frame = Frame(gui)
create_password_frame.pack(fill="both")

# MyPassword Frame
my_password_frame = Frame(gui)
my_password_frame.pack(fill="both")

# Add the Tabs
pages.add(create_password_frame, text="Create Password")
pages.add(my_password_frame, text="Check my Passwords")

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Create password ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Create my TOP Frame
paswword_L_frame = LabelFrame(create_password_frame , text="Adding Password", font=DEFAULT_FONT_STYLE)
paswword_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

Label(paswword_L_frame,text="Username").grid(row=1, column=0, padx=10)
username_entry = Entry(paswword_L_frame, font=DEFAULT_FONT_STYLE)
username_entry.grid(row=1, column=1, padx=30, pady=10, sticky="nsew")

Label(paswword_L_frame,text="Password").grid(row=2, column=0, padx=10)
password_entry = Entry(paswword_L_frame, font=DEFAULT_FONT_STYLE)
password_entry.grid(row=2, column=1, padx=30, pady=10, sticky="nsew")

add_password_button = Button(paswword_L_frame, text="Add")
add_password_button.grid(row=3, column=0, columnspan=2, padx=40, pady=20, sticky="nsew")

error_info_label = Label(create_password_frame, text="TEstTEstTEstTEst", font=DEFAULT_FONT_STYLE)
error_info_label.grid(row=1, column=0, padx=50, pady=20, sticky="nsew")

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Show Password ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Create my TOP Frame
diplay_password_L_frame = LabelFrame(my_password_frame , text="Enter Username", font=DEFAULT_FONT_STYLE)
diplay_password_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

username_test_entry = Entry(diplay_password_L_frame, font=DEFAULT_FONT_STYLE)
username_test_entry.grid(row=1, column=0, padx=70, pady=20, sticky="nsew")

show_password_button = Button(diplay_password_L_frame, text="Show Passwords")
show_password_button.grid(row=2, column=0, padx=40, pady=10, sticky="nsew")

error_info_label = Label(my_password_frame, text="TEstTEstTEstTEst", font=DEFAULT_FONT_STYLE)
error_info_label.grid(row=1, column=0, padx=50, pady=30, sticky="nsew")

gui.mainloop()