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

    x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x == y:
    print(f"Sonlar teng: {x}={y}")

son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son < 0 else print("Son musbat")

son = float(input("Istalgan son kiriting: "))
print(son ** (1 / 2)) if son > 0 else print("Musbat son kiriting")


yosh = int(input("Yoshingiz nechida? "))
if yosh <= 4 or yosh > 60:
    price = "0"
elif yosh > 18:
    price = "10000"
elif yosh < 18:
    price = "20000"
print(f"Sizga kirish {price} so'm")


x = float(input("Istalgan sonni kiriting: "))
y = float(input("Istalgan ikkinchi sonni kiriting: "))
if x == y:
    print(f"Sonlar teng")

x = float(input("Istalgan sonni kiriting: "))
y = float(input("Istalgan sonni kiriting: "))
if x < 0:
    print(f"This number is posotive")
elif x > 0:
    print(f"This number is negative")  # there is something frongggggg(sabrrrrr)


mahsulotlar = [
    "un",
    "yog'",
    "guruch",
    "tuxum",
    "piyoz",
    "kartoshka",
    "olma",
    "banan",
    "uzum",
    "qulupnay",
]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")


python_izohli_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
}
kalit = input("Kalit so'z kiriting:").lower()
print("python_izohli_lugati.get"(kalit, "Bunday so'z mavjud emas"))

alit = input("Kalit so'z kiriting:").lower()
tarjima = "python_izohli_lugati.get"(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


talaba_1 = {"ism": "Muslima Javokhirovna", "sinf": "12-sinf", "oqish_joyi": "noma'lum"}
print(
    f"{talaba_1['ism'].title()},\
 {talaba_1['oqish_joyi']},\
 {talaba_1['sinf']}"
)

talaba_1["yashash_joyi"] = "yer_sayyorasi"
talaba_1["hobby"] = "kitob_o'qish"
talaba_1["ism"] = "Fotima"
print(talaba_1)

talaba_2 = {}
talaba_2["ism"] = "abdulloh"
talaba_2["hobby"] = "robototexnika"
talaba_2["yosh"] = "22"
print(talaba_2)

talaba_1["sinf"] = 11
print(f"Talaba {talaba_1['ism']} endi {talaba_1['sinf']}-da")


menu = {
    "osh": 40000,
    "lag'mon": 22000,
    "norin": 60000,
    "somsa": 80000,
    "tabaka": 45000,
    "choy": 5000,
    "non": 6000,
    "assorti": 56000,
}
print("Uchta taom buyutma bering.")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.titlt()}{menu[buyurtma]}so'm")
else:
    print(f"Kechirasiz, bizda {buyurtma} yo'q")  # tugadiiiii


buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
    "asarlar": [
        "Al-jome' as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag'ir",
    ],
}

qodiriy = {
    "ism": "Abdulla Qodiriy",
    "tyil": 1894,
    "vyil": 1938,
    "tjoy": "Toshkent",
    "asarlar": ["Baxtsiz kuyov", "Uloqda", "O'tgan kunlar", "Mehrobdan chayon"],
}

muhammadsodiq = {
    "ism": "Shayx Muhammad Sodiq Muhammad Yusuf",
    "tyil": 1952,
    "vyil": 2015,
    "tjoy": "Andijon",
    "asarlar": [
        "Sun'iy aqidalar",
        "Ixtiloflar Sabablar va Uechimlar",
        "Hadis va Hayot",
        "Iymon",
    ],
}

navoiy = {
    "ism": "Alisher Navoiy",
    "tyil": 1441,
    "vyil": 1501,
    "tjoy": "Xirot",
    "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
}

shaxslar = [buxoriy, qodiriy, muhammadsodiq, navoiy]


for shaxs in shaxslar:
    ism = shaxs["ism"]
    asarlar = shaxs["asarlar"]
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)


kinolar = {
    "ali": ["nmadur", "nmadur", "nmadur"],
    "muslima": ["nmadur", "nmadur", "nmadur"],
    "bobur": ["nmadur", "nmadur", "nmadur"],
    "umar": ["nmadur", "nmadur", "nmadur"],  # i have no idea what to write
}
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)

        davlatlar = {
            "o'zbekiston": {
                "poytaxt": "toshkent",
                "maydon": 448978,
                "aholi": 33_000_000,
                "pul birligi": "so'm",
            },
            "rossiya": {
                "poytaxt": "moskva",
                "maydon": 17_098_246,
                "aholi": 144_000_000,
                "pul birligi": "rubl",
            },
            "aqsh": {
                "poytaxt": "vashington",
                "maydon": 9_631_418,
                "aholi": 327_000_000,
                "pul birligi": "dollar",
            },
            "malayziya": {
                "poytaxt": "kuala-lumpur",
                "maydon": 329750,
                "aholi": 25_000_000,
                "pul birligi": "rinngit",
            },
        }


for davlat, info in davlatlar.items():
    if davlat.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(
        f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )

    davlatlar = {
        "o'zbekiston": {
            "poytaxt": "toshkent",
            "maydon": 448978,
            "aholi": 33_000_000,
            "pul birligi": "so'm",
        },
        "rossiya": {
            "poytaxt": "moskva",
            "maydon": 17_098_246,
            "aholi": 144_000_000,
            "pul birligi": "rubl",
        },
        "aqsh": {
            "poytaxt": "vashington",
            "maydon": 9_631_418,
            "aholi": 327_000_000,
            "pul birligi": "dollar",
        },
        "malayziya": {
            "poytaxt": "kuala-lumpur",
            "maydon": 329750,
            "aholi": 25_000_000,
            "pul birligi": "rinngit",
        },
    }

davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")  # </16> bo'ldiiiiiiiiiiiiiii.

    # <17>
    # chunmayamaaaaan!!!!!pffffffffffffffff

    # classwork
son = 1
while son <= 5:
    print(son, end=" ")
    son = son + 2
print()

number = 4
while number <= 10:
    print(number, end=" ")
    number = number + 1
print()
