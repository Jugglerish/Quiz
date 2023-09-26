print("WELCOME TO THE PYTHON QUIZ 🚀")

quiz_questions = {
  "What does 'print()' function do in Python? : ": "A",
  "How do you define a function in Python? : ": "B",
  "Which data type is used to store a sequence of characters in Python? : ": "C",
  "What is the result of 2 + 2 in Python? : ": "D",
  "What does 'len()' function return in Python? : ": "A"
}

quiz_options = [
    ["A) Displays output to the console", "B) Reads input from the user", "C) Performs mathematical calculations", "D) Declares a variable"],
    ["A) def function_name():", "B) function_name():", "C) func function_name():", "D) define function_name():"],
    ["A) Integer", "B) Float", "C) String", "D) Boolean"],
    ["A) 4", "B) 22", "C) '4'", "D) It's an error"],
    ["A) The length of a string", "B) The maximum value of a list", "C) The square root of a number", "D) The sum of all elements in a list"]
]

def new_game():
    guesses = []
    correct_answers = 0
    que_num = 0

    for question in quiz_questions:
        que_num += 1
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(question)
        print()
        for option in quiz_options[que_num - 1]:
            print(option)
        print()

        guess = input("Select your option (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_answers += check_answer(quiz_questions[question], guess)

    display_score(correct_answers, guesses)

def check_answer(answer, guess):
    if guess == answer:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_answers, guesses):
    print("------------------------------------------------------------")
    print("RESULT")
    print("------------------------------------------------------------")
    print("Answers", end=" ")
    for question in quiz_questions:
        print(quiz_questions[question], end=" ")
    print()

    print("Guesses:", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = (correct_answers / len(quiz_questions)) * 100
    print("YOUR SCORE IS: " + str(score) + "%")

def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

while True:
    new_game()
    if not play_again():
        print("Bye bye!")
        break
