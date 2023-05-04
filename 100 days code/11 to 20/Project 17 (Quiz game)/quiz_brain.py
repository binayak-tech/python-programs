class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """ It checks whether the question bank still has more questions to ask. """

        return self.question_number < len(self.question_list)

    def next_question(self):
        """ This function generates a question and
        asks the user for their answer.
        Then it calls another function to check
        if the user has guessed correct or not. """

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text}. (True/False)?: ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """ This function takes two parameters
         the user answer and the correct answer
         and checks user answer is correct or not,
         it also assigns the score for each correct answer. """

        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!.")
        else:
            print("Sorry! You're wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")

    def final_score(self):
        """ This function generates the final score when the game ends. """

        print("\nGame Over")
        print(f"Your final score is: {self.score}")
