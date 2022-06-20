from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
THEME_FONT = "Arial"

class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg='#ffffff', bg=THEME_COLOR,
                                 highlightthickness=0, font=(THEME_FONT, 10, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="The question goes here.",
                                                     font=(THEME_FONT, 16, 'italic'),
                                                     width=250,
                                                     justify='left',
                                                     anchor='center')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.get_next_question()

        check_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        cross_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='#ffffff')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)
        self.update_score()


    def false_pressed(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)
        self.update_score()


    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='#23AC6C')
        elif not is_right:
            self.canvas.config(bg='#EC5953')
        self.window.after(1000, self.get_next_question)
