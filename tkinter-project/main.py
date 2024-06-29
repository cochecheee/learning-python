# ti kay inter
from tkinter import *

# create window
window = Tk()

window.title("first gui program")
window.minsize(width=500,height=300)

# create componet
label = Label(text="This is a label",font=("Arial",12,"italic"))
# show label
label.pack()

def get_clicked():
    # get text
    str_input = input.get()
    label.config(text=str_input) 
button = Button(text="click",command=get_clicked)
button.pack()

input = Entry(width=50)
input.pack()


# # *args: tuple
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(1,2,3,4,5,6,7))

# # kwargs
# def add(**kwargs):
#     return kwargs["a"] + kwargs["b"]
# print(add(a=1,b=2))

# keep the screen 
window.mainloop()