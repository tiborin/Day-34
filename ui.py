THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            129,
            width=200,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_guestion()


        self.window.mainloop()


    def get_next_guestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end if quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))
        self.score_label.config(text=f"Score: {self.quiz.score}")
        #self.get_next_guestion()

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        #self.get_next_guestion()

    def give_feedback(self,is_right):
        self.answer = is_right
        if self.answer is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_guestion)










