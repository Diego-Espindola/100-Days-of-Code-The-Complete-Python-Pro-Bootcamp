from question_model import Question
from data import question_data


question_bank = [
    Question(question['text'], question['answer']) for question in question_data
]


def main():
    question_1 = Question("is 2 higher than 1?", "True")
    if input(question_1.text) == question_1.answer:
        print("Correct answer")


if __name__ == "__main__":
    main()
