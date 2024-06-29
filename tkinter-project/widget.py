from tkinter import *
from tkinter.messagebox import showinfo

# creating a window
window = Tk()
window.title = "Widgets of Tkinter"
window.minsize(width=500,height=500)
window.config(padx=20,pady=20)

# create a label
label = Label(text="Text")
# show label
label.pack()
# change text
label.config(text="this is new text")

# create button
def do_when_clicked_button():
   showinfo("Information","button got clicked")
button = Button()
button.config(text="click me",command=do_when_clicked_button)
button.pack()



# keep the screen
window.mainloop()