import time

THEME_COLOR = "#375362"
import tkinter
from quiz_brain import QuizBrain


class QuizUi:

    def answer_true(self):

        self.givefeedback(self.quiz.check_answer("true"))

    def givefeedback(self, answer):
        if answer == True:
            self.canvas.config(bg="Green")
            self.score.config(text=f"Score: {self.quiz.score} ")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, self.next_question)

    def next_question(self):
        # could of called still_has_questions function in quiz_brain but playing around with exceptions.
        try:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.id, text=self.quiz.next_question())
        except IndexError:
            self.canvas.itemconfig(self.id, text="Quiz over")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def answer_false(self):

        givefeedback(self.quiz.check_answer("false"))

    def __init__(self, quiz: QuizBrain):
        self.window = tkinter.Tk()
        self.quiz = quiz
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20)
        self.window.config(bg=THEME_COLOR)
        self.canvas = tkinter.Canvas(self.window, width=300, height=250)
        self.id = self.canvas.create_text(150, 125, text=self.quiz.next_question(), width=75,
                                          font=('Arial', 10, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, command=self.answer_true, highlightthickness=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, command=self.answer_false, highlightthickness=0)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.window.mainloop()
