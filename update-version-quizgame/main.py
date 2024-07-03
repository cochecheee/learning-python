from quiz_brain import QuizBrain
from data import question_data
from ui import QuizUI

quiz_brain = QuizBrain(q_list=question_data)
quiz_ui = QuizUI(quiz_brain=quiz_brain)