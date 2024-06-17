from question_model import Question
from question_data import data
from quiz_brain import QuizBrain

# write a for loop
# create Question from each entry of data
# append to question bank
question_bank = []
for item in data:
    new_q = Question(item["text"],item["answer"])
    question_bank.append(new_q)

# create list of question
quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_question():
    quizbrain.next_question()

print("You've completed the quiz.")
print(f"Total: {quizbrain.score}/{quizbrain.q_number}.")

# https://opentdb.com/api_config.php