def load_questions():
    """Load a predefined list of quiz questions."""
    return [
        {
            "question": "What is the capital of INDIA?",
            "choices": ["1. NCR", "2. MUMBAI", "3. DEHLI", "4. NEW DEHLI"],
            "answer": 4,
        },
        {
            "question": "What is the largest planet in our Solar System?",
            "choices": ["1. Earth", "2. Jupiter", "3. Saturn", "4. Mars"],
            "answer": 2,
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "choices": ["1. Gold", "2. Oxygen", "3. Silver", "4. Helium"],
            "answer": 2,
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["1. Charles Dickens", "2. Mark Twain", "3. William Shakespeare", "4. J.K. Rowling"],
            "answer": 3,
        },
        {
            "question": "What is the square root of 16?",
            "choices": ["1. 2", "2. 3", "3. 4", "4. 5"],
            "answer": 3,
        },
    ]


def ask_question(question, choices, correct_answer):
    """Ask a single question and provide feedback."""
    print("\n" + question)
    for choice in choices:
        print(choice)

    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer < 1 or user_answer > len(choices):
                print("Invalid option. Please choose a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
        return False


def run_quiz():
    """Run the quiz and display the final score."""
    questions = load_questions()
    score = 0

    print("\nWelcome to the Mini Quiz App!")
    print("Answer the following multiple-choice questions:\n")

    for idx, question_data in enumerate(questions, start=1):
        print(f"Question {idx}:")
        if ask_question(question_data["question"], question_data["choices"], question_data["answer"]):
            score += 1

    print("\nQuiz Completed!")
    print(f"Your final score is {score}/{len(questions)}.")

    return score


def main():
    """Main function to control the quiz flow."""
    while True:
        run_quiz()
        retry = input("\nDo you want to retake the quiz? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
