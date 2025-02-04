from abc import ABC, abstractmethod
import random

# Базовый абстрактный класс Hero
class Warrior(ABC):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    # Абстрактный метод для атаки
    @abstractmethod
    def attack(self, other):
        pass

    # Абстрактный метод для проверки жизни
    @abstractmethod
    def is_alive(self):
        pass


# Конкретный класс Warrior, который наследуется от Hero
class Hero(Warrior):
    def __init__(self, name):
        super().__init__(name)  # Вызываем конструктор родительского класса
        self.damage = random.randint(1, 30)  # Случайный урон

    # Реализация метода attack
    def attack(self, other):
        other.health -= self.attack_power
        print(f"Воин {self.name} атаковал {other.name} и нанес {self.attack_power} баллов урона. \n Здоровье {other.name} {other.health}")
        if not other.is_alive():
            print(f"Воин {other.name} умер.")
        else:
            self.health -= self.damage
            print(f"Воин {other.name} атаковал {self.name} и нанес {self.damage} баллов урона. \n Здоровье {self.name} {self.health}")

    # Реализация метода is_alive
    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self):
        self.player = Hero("Добрыня")
        self.computer = Hero("Горыныч")

    def start(self):
        print("Начинается битва!\n")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                break
            self.computer.attack(self.player)

        if self.player.is_alive():
            print(f"Победил {self.player.name}")
        else:
            print(f"Победил {self.computer.name}")

# Главная функция
def main():
    game = Game()
    game.start()

# Запуск программы
if __name__ == "__main__":
    main()