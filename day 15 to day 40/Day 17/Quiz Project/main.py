from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = [
    Question(question['text'], question['answer']) for question in question_data
]

random.shuffle(question_bank)


def main():
    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("You've completed the quiz")
    print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")


if __name__ == "__main__":
    main()
