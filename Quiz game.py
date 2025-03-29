#Harry Potter Quiz Game

questions = ("What is the name of the Weasley family’s home?",
             "Who was the first goblin Harry ever met?",
             "What does the spell Lumos do?",
             "What is the name of Hagrid’s pet dragon in Harry Potter and the Sorcerer’s Stone?",
             "Which potion allows the drinker to take the form of someone else?",
             "What is the core of Harry Potter’s wand?",
             "Who was the Half-Blood Prince?",
             "What is the name of the house elf that serves the Malfoy family?",
             "Which magical creature is known for guarding Gringotts Bank?",
             "What does the Mirror of Erised show?")

options = (("A. The Burrow", "B. Grimmauld Place", "C. Shell Cottage", "D. Godrics Hollow"),
           ("A. Griphook", "B. Bogrod", "C. Ragnok", "D. Gornuk"),
           ("A. Opens locked doors", "B. Summons objects", "C. Produces light from the wand", "D. Creates a protective shield"),
           ("A. Norbet", "B. Fawkes", "C. Buckbeak", "D. Aragog"),
           ("A. Veritaserum", "B. Amortentia", "C. Felix Felicis", "D. Polyjuice potion"),
           ("A. Dragon heartstring", "B. Phoenix feather", "C. Unicorn hair", "D. Basilisk fang"),
           ("A. Tom Riddle", "B. Severus Snape", "C. Sirius Black", "D. Albus Dumboldore"),
           ("A. Dobby", "B. Kreacher", "C. Winky", "D. Hokey"),
           ("A. Thestral", "B. Basilisk", "C. Hungrarian Horntail", "D. Dragon"),
           ("A. The future", "B. The person's deepest desire", "C. The viewers last dream", "D. A warning of impending danger"))

answers = ("A", "A", "C", "A", "D", "B", "B", "A", "D", "B")

guesses = []

question_num = 0
score = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
    question_num += 1

print("")
print("------------------------------")
print("------------RESULTS-----------")
print("------------------------------")
print("")

score = score / 10 * 100

print(f"Your score is {score}%")