from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=250, bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text=f"text", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=tick_image, highlightthickness=0, command=self.button_press_tick)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=cross_image, highlightthickness=0, command=self.button_press_cross)
        self.wrong_button.grid(column=1, row=2)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz! Your final score is {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def button_press_tick(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def button_press_cross(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
