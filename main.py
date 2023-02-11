from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json

window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="white")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def passGenerator ():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    input3.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    websiteinput= input1.get()
    emailinput = input2.get()
    passinput = input3.get()

    new_data={
        websiteinput:{
            "email": emailinput,
            "password": passinput,
         }
    }

    if len(websiteinput) == 0 or len(emailinput) == 0 or len(passinput) == 0:
        messagebox.showerror(message="Please don't leave any filed empty!")
    else:
        # Mode a stand for Append
        # is_ok = messagebox.askokcancel(message="Are you sure?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving the new data
                json.dump(data, data_file, indent=4)
        finally:
            input1.delete(0, END)
            input2.delete(0, END)
            input3.delete(0, END)
            # with open("Password.txt", mode="a") as file:
            #     file.write(f"web: {websiteinput} | email/name: {emailinput} | pass: {passinput}\n")
            #     input1.delete(0, END)
            #     input2.delete(0, END)
            #     input3.delete(0, END)

def search():
        websiteinput = input1.get()
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
                print(data)
        except FileNotFoundError:
            messagebox.showerror(title=websiteinput, message="Doesn't Found")
        else:
            if websiteinput in data:
                messagebox.showinfo(title=websiteinput, message="Email:"+data[websiteinput]["email"] + "\n Password:" +
                                                                data[websiteinput]["password"] )
            else:
                messagebox.showerror(title=websiteinput, message="Doesn't Found")
# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

websiteL = Label(text="Website:", font=("Arial", 10), bg="white")
websiteL.grid(column=0, row=1)
buttonS = Button(text="Search", command=search)
buttonS.grid(column=2, row=1)
# To make the crosier start here
websiteL.focus()
input1 = Entry(width=20)
input1.grid(column=1, row=1, columnspan=2)

emailL = Label(text="Email/Username:", font=("Arial", 10), bg="white")
emailL.grid(column=0, row=2)
input2 = Entry(width=37)
input2.grid(column=1, row=2, columnspan=2)

passwordL = Label(text="Password:", font=("Arial", 10), bg="white")
passwordL.grid(column=0, row=3)
input3 = Entry(width=26)
input3.grid(column=1, row=3)


buttonG = Button(text="Generate Password", command=passGenerator)
buttonG.grid(column=2, row=3)

buttonAdd = Button(text="Add", width=36, command=save)
buttonAdd.grid(column=1, row=4, columnspan=2)
window.mainloop()
