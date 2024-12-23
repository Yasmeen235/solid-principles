class Bird:
    def make_sound(self):
        return "Chirp!"

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class NonFlyingBird(Bird):
    def swim(self):
        return "I can swim!"

class Sparrow(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    pass


sparrow = Sparrow()
print(sparrow.fly())

penguin = Penguin()
print(penguin.swim())
