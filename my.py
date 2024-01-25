# Bismillah


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter ( A, B, C, or D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------")
    print("Results!")
    print("-------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")

    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(questions.get(i), end="")

    print()

    score = (correct_guesses / len(questions)) * 100
    print("Your score is : " + str(score) + "%")


def play_again():
    response = input("Do you want to  play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Iymonning nechta farzi bor? ": "A",
    "Kema yasagan payg'ambar kim? ": "C",
    "Payg'ambarimizning nechta farzandlari bo'lgan? ": "B",
    "Hozirgi hijriy sana? ": "D",
}

options = [
    ["A. 7", "B. 4", "C. 3", "D. 9"],
    ["A. Lut a.s.", "B. Muso a.s.", "C. Nuh a.s.", "D. Yunus a.s."],
    ["A. 4", "B. 7 ", "C. 3", "D. 9"],
    [
        "A. 1442  2-ramazon",
        "B. 1441  14-shavvol",
        "C. 1352 23-rajab",
        "D. 1444 4-sha'bon",
    ],
]

new_game()


while play_again():
    new_game()

print("Bye! Don't forgot to smile ) cuz your smile is beautiful!")
