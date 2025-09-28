from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def Save():
    saved_text = f"{website_input.get()}|{login_input.get()}|{password_input.get()}\n"

    if len(website_input.get()) == 0 or len(login_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Warning", message="Complete all fields")
    else:
        verified = messagebox.askokcancel(title="Confirmation", message=f"You have entered the following details:"
                                                                        f"\n\nWebsite:{website_input.get()}"
                                                                        f"\nLogin:{login_input.get()}"
                                                                        f"\nPassword:{password_input.get()}"
                                                                        f"\n\nConfirm and continue?")
        if verified:
            with open("data.txt", "a") as d:
                d.write(saved_text)
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=250, height=250)
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

login_input = Entry(width=52)
login_input.grid(column=1, row=2, columnspan=2)
login_input.insert(0, "###")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=Save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
