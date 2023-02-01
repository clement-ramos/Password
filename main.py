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

def password_check():  
    password = password_entry.get()

    special_char = ['$', '@', '#', '%', '*', '&', '~', '§', '!', '?', '/', '>', '<', ',', ';', '.', ':', 'µ', '£']
    lower = 0
    alpha = 0
    number = 0
    count_special_char = 0
    len_mdp = len(password)

    for letter in password:
        if letter.isalpha():
            alpha += 1
        if letter.islower():
            lower += 1
        if letter in special_char:
            count_special_char += 1
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number += 1

    if lower != 0 and alpha != 0 and number != 0 and count_special_char != 0 and len_mdp > 7:
        return True
    else:
        return False


def encrypt(password):
    code_encrypt = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return code_encrypt


def add_password():
    username = username_entry.get()
    if password_check():
        password_checked = password_entry.get()
        password_encrypt = encrypt(password_checked)

        if not username in user_dict:
            user_dict[username]= [password_encrypt]

        if not password_encrypt in user_dict[username]:
            user_dict[username].append(password_encrypt)

        messagebox.showinfo("Success", "Password added successfully.")
    else:
        pass
        messagebox.showinfo("Error Password", "Please choose a password who have at least: \n- 1 Uppercase letter \n- 1 Lowercase letter \n- 1 Special characters \n- 1 Number \n- At least a lenght of 7")

    # 3. Write json file
    with open("password.json", "w") as file:
        json.dump(user_dict, file, indent=4)

def show_passwords():
    show_password_list.delete(0, END)
    username = username_test_entry.get()
    nb_of_element = len(user_dict[username])
    if username in user_dict:
        i = 0
        while i < nb_of_element:
            show_password_list.insert(END, user_dict[username][i])
            i += 1




"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI general and notebook ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

gui = Tk()
gui.title("Passwords Manager")
gui.geometry("400x400")
gui.resizable(False, False)

with open('password.json', 'r') as file:
    user_dict = json.load(file)

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

add_password_button = Button(paswword_L_frame, text="Add", command=add_password)
add_password_button.grid(row=3, column=0, columnspan=2, padx=40, pady=20, sticky="nsew")

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Show Password ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Create my TOP Frame
diplay_password_L_frame = LabelFrame(my_password_frame , text="Enter Username", font=DEFAULT_FONT_STYLE)
diplay_password_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

username_test_entry = Entry(diplay_password_L_frame, font=DEFAULT_FONT_STYLE)
username_test_entry.grid(row=1, column=0, padx=70, pady=20, sticky="nsew")

show_password_button = Button(diplay_password_L_frame, text="Show Passwords", command=show_passwords)
show_password_button.grid(row=2, column=0, padx=40, pady=10, sticky="nsew")

show_password_list = Listbox(diplay_password_L_frame)
show_password_list.grid(row=3, column=0, padx=40, pady=10, sticky="nsew")

gui.mainloop()