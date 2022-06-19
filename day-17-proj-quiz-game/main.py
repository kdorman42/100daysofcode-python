from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# no need to use range
# for q in range(0, len(question_data)):
#     qq = Question(question_data[q]["text"], question_data[q]["answer"])
#     question_bank.append(qq)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    player_answer = quiz.next_question()

print("You've completed the quiz.")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')



