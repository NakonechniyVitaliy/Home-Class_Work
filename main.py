class Car:

    def __init__(self, model, year, volume, color, price):
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.price = price

    def show(self):
        return(f"\nМодель: {self.model} \n"
               f"Год: {self.year} \n"
               f"Обьём: {self.volume} \n"
               f"Цвет: {self.color} \n"
               f"Цена: {self.price}")


car_1 = Car("BMW", "2000", "500", "Black", "5000$")
print(car_1.show())

################################################################################

class Book:

    def __init__(self, name, year, publisher, genre, autor, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def show(self):
        return(f"\nИмя: {self.name}\n"
               f"Год: {self.year}\n"
               f"Издатель: {self.publisher}\n"
               f"Жанр: {self.genre}\n"
               f"Автор: {self.autor}\n"
               f"Цена: {self.price}")

book_1 = Book("Flower", "2019", "Booooks", "Триллер", "Елена В.Г.", "25$")
print(book_1.show())

################################################################################

class Stadion:

    def __init__(self,name,year,country,city,size):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.size = size

    def show(self):
        return(f"\nНазвание: {self.name}\n"
               f"Год: {self.year}\n"
               f"Страна: {self.country}\n"
               f"Город: {self.city}\n"
               f"Вместимость: {self.size}")

stadion_1 = Stadion("Донбасс Арена","2009","Украина","Донбас","50 000")
print(stadion_1.show())