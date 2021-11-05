class Students:
    subject = ["Math", "Physics", "Programming"]
    mark = [4, 5, 3]

    def ch_mark(self, Mark):
        self.mark = Mark

    def ch_subject(self, new_Subject):
        self.subject = new_Subject


def change_mark():
    new_mark = []
    print("введите количество оценок")
    n_mark = int(input())
    print("введите оценки")
    while n_mark > 0:
        n_mark = n_mark - 1
        new_mark.append(input())
    Egor.ch_mark(new_mark)


def change_subject():
    new_subject = []
    print("введите количество предметов")
    n_subjects = int(input())
    print("введите предметы")
    while n_subjects > 0:
        n_subjects = n_subjects - 1
        new_subject.append(input())
    Egor.ch_subject(new_subject)


Egor = Students()
while 1:
    choice = int(input())
    if choice == 1:
        print(Egor.subject)
    elif choice == 2:
        print(Egor.mark)
    elif choice == 3:
        change_subject()
    elif choice == 4:
        change_mark()
    print("\n")
