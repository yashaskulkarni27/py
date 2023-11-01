class person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def greeting(self):
        print(f"Hello {self.name}")

person1 = person(1, "Abdul")
person1.greeting()

