class Person:
def __init__(self,name,age):
    self.name=name;
    self.age=age;

p1=Person("suppandi",14)

print("\n name of person #1 is",p1.name)
print("\n age of person #1 is",p1.age)

print("\n **after deletion ")
del p1.age

print("\n name of person #1 is",p1.name)

print("\n **after deletion ")
del p1

print("\n name of person #1 is",p1.name)