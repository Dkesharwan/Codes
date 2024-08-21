class Grandparents:
    def owner(self):
        print("I m the owner of the house")


class Parents(Grandparents):
    def __init__(self):
        print("I m the second owner of the house")
        self.house = 2

    def special_property(self):
        print("I have to listen everyone terms and condition")


class Child(Parents):

    def __init__(self):
        print("I m the youngest one in the family")

        self.house = 0

    def special_property(self):
        print("Everyone listen my terms and condition")


Ram = Parents()
Ram.owner()
Ram.special_property()

Ramlal = Grandparents()
Ramlal.owner()
Shyam = Child()
Shyam.special_property()
Shyam.owner()

print(isinstance(Ram, Parents))
print(isinstance(Shyam, Parents))

print(issubclass(Parents, Grandparents))
print(issubclass(Child, Parents))