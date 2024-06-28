from tkinter import *
from tkinter import messagebox
import randompass

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# ------------------------------------- GENERATE A PASSWORD
def generate_password():
    new_pass = randompass.gen_pass()
    pass_input.delete(0,END)
    pass_input.insert(0,new_pass)

# ------------------------------------- SAVE DATA TO FILE
def save_file(website,username,password):
    with open("data.txt",mode="a") as file:
        data = f"{website} | {username} | {password}\n"
        file.writelines(data)
    
def add_account():
    website = website_input.get()
    username = username_input.get()
    password = pass_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please fill in all entry fields...")
    else:
        # yes or no if they want to save file
        message = f"These are details entered:\n Website: {website}\n Username: {username}\n Password: {password}"
        is_ok = messagebox.askokcancel(title=website,message=message)

        # save file
        if is_ok:
            save_file(website=website,username=username,password=password)
            # delete data in entry
            delete_entry()

def delete_entry():
    website_input.delete(0,END)
    # cuz we often use same mail or username so it is good to not delete that
    # username_input.delete(0,END)
    pass_input.delete(0,END)
    website_input.focus()

# -------------------------------------- UI SET UP
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# # create 3 label 
website_lbl = Label(text="Website")
username_lbl = Label(text="Email/Username")
pass_lbl = Label(text="Password")

website_lbl.grid(row=1,column=0)
username_lbl.grid(row=2,column=0)
pass_lbl.grid(row=3,column=0)

# # create 3 input fields
website_input = Entry(width=35)
username_input = Entry(width=35)
pass_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)
username_input.grid(row=2,column=1,columnspan=2)
pass_input.grid(row=3,column=1)

# # create button
gen_pass_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add",width=36,command=add_account)
gen_pass_btn.grid(row=3,column=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()