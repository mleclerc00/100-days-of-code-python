from tkinter import Button, Canvas, Label, PhotoImage, Tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """init method for UI class

        Args:
            quiz_brain (QuizBrain): The QuizBrain object
        """
        # Create the quiz brain
        self.quiz = quiz_brain

        # Create the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        # Create the canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create the buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        # Create the score
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Get the first question
        self.get_next_question()

        # Bind the buttons
        self.true_button.config(command=self.true_pressed)
        self.false_button.config(command=self.false_pressed)

        # Bind the answer
        self.answer = self.window.register(self.get_answer)

        # Start the window
        self.window.mainloop()

    def get_next_question(self):
        """Gets the next question in the quiz and updates the UI, or ends the quiz if there are no more questions"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz, congratulations!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.update_score()

    def update_score(self):
        """Updates the score label"""
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        """Handles the user pressing the true button, checks the answer, and gives feedback"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Handles the user pressing the false button, checks the answer, and gives feedback"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        """Gives the user feedback on their answer and gets the next question

        Args:
            is_right (bool): True if the user's answer was correct, False otherwise
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_answer(self) -> str:
        """Gets the user's answer

        Returns:
            str: The user's answer
        """
        return self.window.wait_variable(self.answer)
