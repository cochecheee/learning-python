# https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean
import requests
from question_model import Question

# 1. request data from api
response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')

# 2. parse to dict through json data format
data = response.json()['results']

# 3. just add need data
question_data = []
for item in data:
    a_ques =  Question(text=item['question'],answer=item['correct_answer'])
    question_data.append(a_ques)
