class Students:
    subject = ["Math", "Physics", "Programming"]


Egor = Students()
while 1:
    choice = int(input())
    if choice == 1:
        print(Egor.subject)
