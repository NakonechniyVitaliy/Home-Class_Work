class Employed():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_employed(self):
        print("This is Employed class")



class President(Employed):

    def print_employed(self):
        print(f"Президент {self.name} керує країною")
    def __str__(self):
        return f"Президент {self.name} керує країною"
    def __int__(self):
        return f"Вік - {self.age}"


class Manager(Employed):

    def print_employed(self):
        print(f"Менеджер {self.name} керує робітниками")
    def __str__(self):
        return f"Менеджер {self.name} керує робітниками"
    def __int__(self):
        return f"Вік - {self.age}"

class Worker(Employed):

    def print_employed(self):
        print(f"Робітник {self.name} виконує свою роботу")
    def __str__(self):
        return f"Робітник {self.name} виконує свою роботу"
    def __int__(self):
        return f"Вік - {self.age}"




prezident = President("Петро",45)
manager = Manager("Ігор",33)
worker = Worker("Сергій",19)

prezident.print_employed()
manager.print_employed()
worker.print_employed()
print("\n Далі йде вивід через __str__\n")
print(prezident.__str__(),"\n", prezident.__int__())
print(manager.__str__(),"\n", manager.__int__())
print(worker.__str__(),"\n", worker.__int__())

#######################################################################

class math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a-b

    @staticmethod
    def dil(a, b):
        return a/b

    @staticmethod
    def mno(a, b):
        return a*b

print("\nMath:")
print(math.plus(20, 10))
print(math.minus(20, 10))
print(math.dil(20, 10))
print(math.mno(20, 10))
