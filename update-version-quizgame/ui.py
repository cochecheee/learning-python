from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    # 1.first build when you create am QuizUI object
    def __init__(self,quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz app")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", fg="white",background=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text", fill='black',font=('Arial',12,'italic'),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file="./image/true.png")
        self.true_button = Button(image=true_img,highlightthickness=0,command=self.true_check)
        self.true_button.grid(row=2,column=0)
        
        false_img = PhotoImage(file="./image/false.png")
        self.true_button = Button(image=false_img,highlightthickness=0,command=self.false_check)
        self.true_button.grid(row=2,column=1)

        self.show_score()
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.show_score()
        if self.quiz.still_has_question() == True:
            # still have question
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else: 
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text,text=f"Congratulation! You've got {self.quiz.score} out of {self.quiz.q_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_still_have_question(self) -> bool:
        return self.quiz.still_has_question()
    
    def true_check(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_check(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        
    def show_score(self):
        self.score_label.config(text=f"Score: {self.quiz.get_score()}")
