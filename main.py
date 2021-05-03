from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
WHITE = "#FFFFFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure if any of the fields are empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user_name}"
                                   f"Password: {password} \n Do you want to save?")
        if is_ok:
            f = open("passwords.txt", "a")
            f.write(f"{website} | {user_name} | {password}\n")
            f.close()
            website_entry.delete(0, END)
            user_name_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#website_text
website_text = Label(text="Website:", bg=WHITE)
website_text.grid(row=1, column=0)
#user_name/email_test
user_name_text = Label(text= "Email/Username:", bg=WHITE)
user_name_text.grid(row=2, column=0)
#password_text
password_text = Label(text="Password:", bg=WHITE)
password_text.grid(row=3, column=0)

#website_entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
#user_name/email_entry
user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "adorablevardan@gmail.com")
#password_entry
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

#generate_password_button
password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

#add_text
add_text = Button(text="Add", width=30, highlightthicknes=0, command=save)
add_text.grid(column=1, row=4, columnspan=2)

window.mainloop()

