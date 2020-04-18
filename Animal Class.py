#LEARNING CLASSES AND OBJECTS
# I created a parent class of Animal which has three child classes Cat, Rabbit and Person.
# The person class has a child class named Student.
# All these classes have a variety of mehtods and Properties as well as methods they all inherit from their parent classes.



class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__ (self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name)+":"+str(self.age)

class rabbit(Animal):
    tag = 1
    def __init__ (self, age, parent1=None, parent2 = None):
        Animal. __init__ (self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = rabbit.tag
        rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:" + str(self.name)+":"+str(self.age)
    def __add__ (self,other):
        return rabbit(0, self, other)
    def __eq__ (self,other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

class Person(Animal):
    def __init__ (self,name,age):
        Animal. __init__ (self,age)
        Animal.set_name(self,name)
        self.friends = []
    def get_friends (self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        #alternative way :diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(other.name, "is", -diff, "years older than", self.name)

    def speak (self):
        print("hello")
    def __str__ (self):
        return "Person:" + str(self.name) + ":" + str(self.age)


class Student(Person):
    def __init__ (self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major (self, major):
        self = major
    def speak(self):
        r=random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__ (self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
