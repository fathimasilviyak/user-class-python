class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("I can breathe")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("I can swim")

    def breathe(self):
        super().breathe()
        print("only underwater.")


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)