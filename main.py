class Person:
  def __init__(self, name: str, age: int, id: str):
    self.name = name
    self.age = age
    self.id = id


  def __eq__(self, other):
    return (self.id == other.id) & (self.name == other.name)



person1 = Person("bahadir",28,"x7")
person2 = Person("fatma",26, "x7")

print(person1 == person2)