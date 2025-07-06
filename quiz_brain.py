
class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_question(self,choice,answer ):

        if choice.lower()==answer.lower():
            print("you got it right!")
            self.score+=1
        else:
            print("That's Wrong")
            print(f"The correct answer is {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        choice=input(f"Q{self.question_number}: {question.text} Enter True\False")
        self.check_question(choice,question.answer)
