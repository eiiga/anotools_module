from abc import ABC, abstractmethod


class Animal(ABC):
    # サブクラスで必ずオーバーライドさせたいメソッドを定義
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "ワン！"


if __name__ == '__main__':
    dog = Dog()
    print(dog.speak())
