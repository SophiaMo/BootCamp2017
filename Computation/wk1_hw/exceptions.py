#expections.py
"""Exceptions
Sophia Mo
06/26/2017
"""
#Problem 1
def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last ""digits differ by 2 or more: ")
    if len(str(step_1)) != 3:
        raise ValueError("input should be 3-digits")
    if int(str(step_1)[2])-int(str(step_1)[0])<2:
        raise ValueError("first and last digits should differ by at least 2")
    step_2 = input("Enter the reverse of the first number, obtained ""by reading it backwards: ")
    if str(step_2)[2]!=str(step_1)[0] or str(step_2)[1]!=str(step_1)[1] or str(step_2)[0]!=str(step_1)[2]:
        raise ValueError("this is not the reverse of the first number")
    step_3 = input("Enter the positive difference of these numbers: ")
    if int(str(step_3)) != int(str(step_2))-int(str(step_1)):
        raise ValueError("this is not the difference of the two numbers")
    step_4 = input("Enter the reverse of the previous result: ")
    if int(str(step_4)[2])!=int(str(step_3)[0]) or int(str(step_4)[1])!=int(str(step_3)[1]) or int(str(step_4)[0])!=int(str(step_3)[2]):
        raise ValueError("this is not the reverse of the previous result")
    print(str(step_3) + " + " + str(step_4) + " = 1089 (ta-da!)")

#Problem 2
from random import choice
def random_walk(max_iters=1e12):
    try:
        walk = 0
        direction = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(direction)
    except KeyboardInterrupt:
            print("Process interrupted at iteration "+str(i))
    finally:
            print(str(walk))

#Problem 3
class ContentFilter:
    def __init__(self, name):
        try:
            with open(name) as myfile:
                self.name = name
                self.contents = myfile.read()
        except:
            isinstance(name,str)==False
            raise TypeError("file name is not the correct type")
#Problem 4
    def uniform(self, name, mode="w", case="upper"):
        if mode!="w" and mode!="a":
            raise ValueError("file mode is not the correct type")
        if case!="upper" and case!="lower":
            raise ValueError("case should be either upper or lower")
        if case == "upper":
            with open(name,'w') as myfile:
                myfile.write(self.contents.upper())
        if case == "lower":
            with open(name,'w') as myfile:
                myfile.write(self.contents.lower())

    def reverse(self, name, mode="w", unit="line"):
        if mode!="w" and mode!="a":
            raise ValueError("file mode is not the correct type")
        if unit!="line" and unit!="word":
            raise ValueError("unit should be either line or unit")
        if unit == "line":
            with open(name,'w') as myfile:
                lines = self.contents.split('\n')
                lines = lines[::-1]
                myfile.write(str(lines))
        if unit == "word":
            with open(name,'w') as myfile:
                words = self.contents.split(" ")
                words = words[::-1]
                myfile.write(str(words))

    def transpose(self, name):
        with open(name, 'w') as myfile:
            lis = [x.split() for x in self.contents]
            lis_1 = zip(*lis)
            myfile.write(str(lis_1))

    def __str__(self):
        return '\n Source file: \t{} \n Total characters: \t{} \n Alphabetic characters: \t{} \n Numerical characters: \t{} \n Whitespace characters: \t{} \n Number of lines: \t{} \n'.format(self.name, len(self.contents), sum(x.isalpha() for x in self.contents), sum(x.isdigit() for x in self.contents), sum(x.isspace() for x in self.contents), sum(1 for line in self.contents))
