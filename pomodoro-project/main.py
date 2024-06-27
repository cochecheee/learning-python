# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 4
timer = None

from tkinter import *
from math import floor

# RESET
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text,text="0:00")
    label_cm.config(text="")


# COUNTDOWN
def count_down(count):
    minute = floor(count/60)
    second = count % 60

    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text,text=f"{minute}:{second}")
    if count > 0:
        global timer 
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps/2)):
            marks += "✔"
        label_cm.config(text=marks)

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        label.config(text="Work")
        count_down(work_sec)
    elif reps == 8: 
        label.config(text="Break",fg=RED)
        reps=0
        count_down(long_break_sec)
    else:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# UI SET UP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# set up the title
label = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,background=YELLOW)
label.grid(column=1,row=0)

# set up image and timer countdown
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00",font=(FONT_NAME,35,"bold"),fill ="white")
canvas.grid(row=1,column=1)

# set up 2 buttons START and RESET
button_start = Button(text="Start",command=start_timer)
button_start.grid(row=2,column=0)

button_reset = Button(text="Reset",command=reset)
button_reset.grid(row=2,column=2)

# set up checkmark
label_cm = Label(bg=YELLOW,fg=GREEN)
label_cm.grid(row=3,column=1)
window.mainloop()