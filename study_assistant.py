import random
import time

# ---------------- QUESTION BANK ----------------

question_bank = {
    "Python": {
        "What is a list?": "collection",
        "Which keyword defines a function?": "def",
        "What does len() do?": "length",
        "What data type is returned by input()?": "string",
        "What symbol is used for comments in Python?": "#",
        "Which loop is used to iterate over a sequence?": "for"
    },

    "Computer Basics": {
        "What does CPU stand for?": "central processing unit",
        "What does RAM stand for?": "random access memory",
        "What is the brain of the computer?": "cpu",
        "What does OS stand for?": "operating system",
        "Which device is used to type?": "keyboard"
    },

    "Math": {
        "What is 10 + 5?": "15",
        "What is 12 x 2?": "24",
        "What is the square of 4?": "16",
        "What is 20 divided by 5?": "4",
        "What is 9 + 6?": "15"
    }
}

# ---------------- FUNCTIONS ----------------

def show_menu():
    print("\n=== Personal Study Assistant ===")
    print("1. Take Quiz")
    print("2. Study Timer")
    print("3. Exit")


def flashcard_quiz():
    print("\nChoose a topic:")
    topics = list(question_bank.keys())

    for i in range(len(topics)):
        print(f"{i + 1}. {topics[i]}")

    choice = int(input("Enter topic number: ")) - 1
    selected_topic = topics[choice]

    questions = question_bank[selected_topic]
    question_list = list(questions.keys())

    score = 0
    total_questions = min(3, len(question_list))
    selected_questions = random.sample(question_list, total_questions)

    print(f"\nStarting quiz on {selected_topic}...\n")

    for question in selected_questions:
        user_answer = input(question + " ")
        correct_answer = questions[question]

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is:", correct_answer, "\n")

    print(f"Your score: {score}/{total_questions}")


def study_timer():
    minutes = int(input("Enter study time in minutes: "))
    print("Focus time started...")
    time.sleep(minutes * 60)
    print("Time's up! Take a break 😊")


# ---------------- MAIN PROGRAM ----------------

while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        flashcard_quiz()
    elif option == "2":
        study_timer()
    elif option == "3":
        print("Goodbye! Happy studying 💙")
        break
    else:
        print("Invalid choice. Try again.")
