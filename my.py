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
]  # so, here in optios you can put your own question and answers just simly to change them


new_game()


while play_again():
    new_game()

print("Bye! Don't forgot to smile ) cuz your smile is beautiful!")


t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2023 - t_yil
print("Siz " + str(yosh) + " yoshda ekansiz")


son = int(input("Istalgan sonni kiriting\n>>>"))
hisob = son**2
print(str(hisob) + " " + "ga teng")  # not yet

yosh = int(input("Yoshingiz nechchida?:\n>>>"))
hisob = 2024 - yosh
print("Siz" + " " + str(hisob) + " " + "yilda tug'ilgansiz")


countries = [
    "Uzbekistan",
    "Saudia",
    "Malaysia",
    "US",
    "Canada",
    "Germany",
    "Turkey",
    "Moscow",
    "Afghanistan",
    "Pakistan",
    "Switzerland",
]
print("Total number of countries: ", len(countries))
print(sorted(countries))
print(sorted(countries, reverse=True))
print(countries.reverse())
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)


narhlar = [12000, 225000, 34000, 45000]
eng_arzon = min(narhlar)
eng_qimmat = max(narhlar)
jami = sum(narhlar)
narhlar[0] = int(narhlar[0] - narhlar[3])
print("Elementlarning soni:", len(narhlar))
print("Eng arzon narh ", eng_arzon, ".Eng qimmat narh", eng_qimmat, ".Jami:", jami)
print(narhlar)


friends = ["Yulduz", "Muslimakhon", "Muslimaaa", "Suhaila"]
for friend in friends:
    print(f"Qardrdon do'stim {friend},sizni 5-fevral kuni kinoga taklif qilaman!")
    print(" Lovely Muslima")
print("Kod 4 marta takrorlandi")


n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)  # 2

cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())

        cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
for car in cars:
    if car != "gm":
        print(car.upper())
    else:
        print(car.title())  # finally

# help


ism = input("Ismingiz nima?\n>>>")
if ism.lower() != "muslima":
    print(f"Xush kelibsiz" + " " + str(ism.title))
else:
    print("Xush kelibsiz Admin, .Foydalanuvchilar ro'yxatini ko'rishni istaysizmi?")

    login = input("Login kiriting: ")
if login.lower() == "admin":
    print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login.title()}!")
