class QuizBrain:
    def __init__(self, question_list, question_number=0):
        self.question_number = question_number
        self.question_list = question_list
        self.score = 0
    def display(self):
        print("elo")

    def next_question(self):

        question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input("Q."+ str(self.question_number) + ": "+question.text + "(True/False)?")
        if choice == question.answer:
            print("brawo!")
            self.score += 1
        else:
            print("źle!")
        print(f"Correct answer was : {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_question(self):

        return len(self.question_list) > self.question_number







