from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    text = key["text"]
    answer = key["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")