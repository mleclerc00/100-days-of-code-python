from html import unescape

from question_model import Question


class QuizBrain:
    def __init__(self, q_list: list[Question]):
        """init method for QuizBrain class

        Args:
            q_list (list[&quot;Question&quot;]): List of Question objects
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self) -> bool:
        """Checks if there are still questions left in the quiz

        Returns:
            bool: True if there are still questions left, False otherwise
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Gets the next question in the quiz

        Returns:
            str: The next question in the quiz
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer: str) -> bool:
        """Checks if the user's answer is correct

        Args:
            user_answer (str): The user's answer

        Returns:
            bool: True if the user's answer is correct, False otherwise
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            self.give_feedback(self.score, self.question_number)
            return True
        else:
            print("That's wrong.")
            self.give_feedback(self.score, self.question_number)
            return False

    def give_feedback(self, score: int, question_number: int):
        """Prints the user's current score

        Args:
            score (int): user's current score
            question_number (int): current question number
        """
        print(f"Your current score is: {score}/{question_number}")
        print("\n")
