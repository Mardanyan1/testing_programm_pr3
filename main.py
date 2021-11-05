class Students:
    subject = ["Math", "Physics", "Programming"]
    mark = [4, 5, 3]


Egor = Students()
while 1:
    choice = int(input())
    if choice == 1:
        print(Egor.subject)
    elif choice == 2:
        print(Egor.mark)
