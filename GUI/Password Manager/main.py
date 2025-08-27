from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"There are details entered: \nEmail: {email}"
                                                  f"\npassword: {email} \nIs it okay to save?" )
    if is_ok :
        if len(email) > 0 and len(password) > 0 and len(website) > 0:
            with open ("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.askokcancel(title="error", message="Please fill all blanks")

# ---------------------------- UI SETUP ------------------------------- #
  
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=150, width=150)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels 
website_label = Label(text="Website:")
website_label.grid(row=1, column=0 )

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0 )

password_label = Label(text="password:")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width = 45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width = 45)
email_entry.grid(row=2, column=1, columnspan=2)


password_entry = Entry(width = 26)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row = 3, column=2)

add_button = Button(text="Add", width = 38, command=save) 
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

