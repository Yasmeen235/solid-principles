class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def fly(self):
        return "I can't fly, but I can swim!"


birds = [Bird(), Penguin()]
for bird in birds:
    print(bird.fly())