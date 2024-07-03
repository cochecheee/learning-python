import html
# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz
class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.current_question = q_list[0]
        self.score = 0
    
    # retrieve the q_num from q_list
    def next_question(self):
        self.current_question = self.q_list[self.q_number]
        self.q_number += 1
        
        # # version 1
        # user_answer = input(f"Q.{self.q_number}: {html.unescape(question.text)}?: ")
        # self.check_answer(user_answer,question.answer)

        # version 2
        return f"Q.{self.q_number}: {html.unescape(self.current_question.text)}?: "
    
    # check if there is any question remains
    def still_has_question(self):
        if self.q_number < len(self.q_list):
            return True
        return False
    
    # check the answer v1
    # def check_answer(self, user_answer, q_answer):
    #     if user_answer.lower() == q_answer.lower():
    #         print("You got it right!")
    #         self.score += 1
    #     else:
    #         print("You got it wrong!")
    #     print(f"The correct answer was {q_answer}.")
    #     print(f"You're current score is {self.score}/{self.q_number}.\n")

    def check_answer(self, user_answer) -> bool:
        
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False
        
    def get_score(self) -> int:
        return self.score