from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for entry in question_data:
    question=Question("text","answer")
    question.text=entry["text"]
    question.answer=entry["answer"]
    question_bank.append(question)


player=QuizBrain(question_bank)
while player.still_has_questions():
    player.next_question()
print("you have completed the quiz")
print(f"Your final score is {player.score}/{player.question_number}")