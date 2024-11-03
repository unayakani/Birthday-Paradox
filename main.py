import random

for _ in range(200):
    birthdays = list()

    for i in range(23):
        date = random.randrange(1, 29)
        month = random.randrange(1, 13)
        birthdays.append((date, month))

    birthday_set = set(birthdays)

    if len(birthday_set) < len(birthdays):
        file = open("result.txt", "a")
        file.write("Match\n")
    else:
        file = open("result.txt", "a")
        file.write("No Match\n")

n_match = int()
n_no_match = int()

with open("result.txt") as result:
    for line in result:
        if line == "Match\n":
            n_match += 1
        else:
            n_no_match += 1

print("Birthday match percentage is: ", (( n_match / (n_match + n_no_match)) * 100), "%")
