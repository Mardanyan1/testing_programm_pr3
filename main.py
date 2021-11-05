class Students:
    subject = ["Math", "Physics", "Programming"]
    mark = [4, 5, 3]

    def ch_mark(self, Mark):
        self.mark = Mark


def change_mark():
    new_mark = []
    print("введите количество оценок")
    n_mark = int(input())
    print("введите оценки")
    while n_mark > 0:
        n_mark = n_mark - 1
        new_mark.append(input())
    Egor.ch_mark(new_mark)


Egor = Students()
while 1:
    choice = int(input())
    if choice == 1:
        print(Egor.subject)
    elif choice == 2:
        print(Egor.mark)
    elif choice == 3:
        change_mark()
