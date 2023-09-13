class Animals:
    def __init__(self):
        self.eyes = 2
        self.limbs = 4

    def walk(self):
        for i in range(1, self.limbs + 1):
            print(f"step {i}")


class Humans(Animals):  # class Humans inherits from class Animals
    def __init__(self):
        super().__init__()  # this line is essential for inheritance to work

    def walk(self):  # to do something special in inheriting classes function use this
        super().walk()  # this means first super classes method
        print("Just using 2 legs")  # then from this method


roby = Humans()

roby.walk()
print(f"Roby has {roby.eyes} eyes and {roby.limbs} limbs")
