from html import unescape
from json import load
from question_model import Question
from quiz_brain import QuizBrain
from urllib import request

with request.urlopen("https://opentdb.com/api.php?amount=10&type=boolean") as url:
    question_data = unescape(load(url))

question_bank: list[Question] = []
for question in question_data["results"]:
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
