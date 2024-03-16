from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.score_label = Label(
            self.window,
            text=f"",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

        right_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(self.window, image=right_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        wrong_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(self.window, image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)

        self.button_clicked = False

        self.get_next_question()

        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.button_clicked = False
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.update_score()
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz\n"
                                                            f"You made {self.quiz.score} out of "
                                                            f"{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        if not self.button_clicked:
            self.button_clicked = True
            self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        if not self.button_clicked:
            self.button_clicked = True
            self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, self.get_next_question)

    def return_color(self, color):
        self.canvas.config(bg="White")
