from tkinter import *
from tkinter import messagebox
import randompass
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ------------------------------------- SEARCH FOR A WEBSITE
def search():
    # take the name of website
    website = website_input.get()

    # get data from json file
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Data File Not Found")
    else:
        if website in data.keys():
            email = data[website]["name"]
            password = data[website]["password"]
            message=f"Email: {email}\nPassword: {password}"
            messagebox.showinfo(title=website,message=message)
        else:
            messagebox.showinfo(title=website,message=f"No account was found for {website}")

# ------------------------------------- GENERATE A PASSWORD
def generate_password():
    new_pass = randompass.gen_pass()
    pass_input.delete(0,END)
    pass_input.insert(0,new_pass)

# ------------------------------------- SAVE DATA TO FILE
def save_file(website,username,password):
    # with open("data.txt",mode="a") as file:
    #     data = f"{website} | {username} | {password}\n"
    #     file.writelines(data)
    new_data = {
        website : {
            "name" : username,
            "password" : password,
        }
    }

    # load data 
    try:
        with open("data.json","r") as data_file:
            # read old data
            data = json.load(data_file)
    except:
        data = {}
        data.update(new_data)
    
    # update and write data
    with open("data.json","w") as data_file:
        # update new data to old data
        data.update(new_data)
        # write to file
        json.dump(data,data_file,indent=4)
    
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
username_input.insert(0,"coche@coche.vn")
website_input.grid(row=1,column=1,columnspan=2)
username_input.grid(row=2,column=1,columnspan=2)
pass_input.grid(row=3,column=1)

# # create button
gen_pass_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add",width=36,command=add_account)
gen_pass_btn.grid(row=3,column=2)
add_btn.grid(row=4, column=1, columnspan=2)
# # # new search button
search_btn = Button(text="Search",padx=10,command=search)
search_btn.grid(row=1, column=2)

window.mainloop()

