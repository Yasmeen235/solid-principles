from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Working...")

    def eat(self):
        print("Eating...")

class Robot(Workable):
    def work(self):
        print("Working...")


worker = Worker()
robot = Robot()

worker.work()
worker.eat()
robot.work()