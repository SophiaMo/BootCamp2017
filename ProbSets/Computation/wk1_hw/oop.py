#oop.py
"""OOP
Sophia Mo
06/26/2017
"""
 import sys
#Problem 1
class Backpack(object):
    """A Backpack object class. Has a name, color, max size, and a list of contents.
    Attributes:
    name (str): the name of the backpack's owner.
    color(str): the color of the backpack.
    max_size(int): the max size of the backpack.
    contents (list): the contents of the backpack.
    """
    def __init__(self, name, color, max_size=5): # This function is the constructor.
        self.name = name
        self.color = color
        self.max_size = int(max_size)
        self.contents = []

    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents)>self.max_size-1:
            raise ValueError("Cannot exceed the max size")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Dump everything in the backpack."""
        del self.contents[:]

    #Problem 3
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color \
        and len(self.contents)==len(other.contents)
    def __str__(self):
        return '''\n Owner: \t{} \n Color: \t{} \n Max size: \t{} \n Contents: \t{} \n'''.format(\
        self.name, self.color, self.max_size, self.contents)

#Problem 2
class Jetpack(Backpack):
    def __init__(self, name, color, max_size=2):
        Backpack.__init__(self, name, color, max_size)
        self.fuel = 10

    def fly(self, fuel):
        if fuel>=self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel=self.fuel-float(fuel)

    def dump(self):
        del self.contents[:]
        self.fuel=0

#Problem 4
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __lt__(self, other):
        return math.sqrt(self.real**2 + self.imag**2)< math.sqrt(other.real**2 + other.imag**2)

    def __gt__(self, other):
        return math.sqrt(self.real**2 + self.imag**2)> math.sqrt(other.real**2 + other.imag**2)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __neq__(self, other):
        return self.imag != other.imag or self.real != other.real

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __div__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)
