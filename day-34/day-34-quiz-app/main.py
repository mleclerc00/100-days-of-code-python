from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create the question bank
question_bank: list[Question] = []

# Populate the question bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question: Question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create the quiz
quiz = QuizBrain(question_bank)

# Create the UI
ui = QuizInterface(quiz)

# Run the quiz
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer(ui.get_answer())
