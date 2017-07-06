#standard_lib.py
"""Standard Library
Sophia Mo
06/26/2017
"""

#Problem 1
def prob_1(l):
    list=[min(l),max(l),float(sum(l)/len(l))]
    return list

#Problem 2
'numbers'
num_1 = 1
num_2 = num_1
num_2 += 1
print(num_1 == num_2)

'strings'
word_1 = "econ"
word_2 = word_1
word_2 += "a"
print(word_1 == word_2)

'lists'
list_1 = [1,2,3,4,5]
list_2 = list_1
list_2.append(1)
print(list_1 == list_2)

'tuples'
tuple_1 = (1,2,3,4,5)
tuple_2 = tuple_1
tuple_2 += (1,)
print(tuple_1==tuple_2)

'dictionaries'
dict_1 = {1:"x",2:"y"}
dict_2 = dict_1
dict_2[1] = "a"
print(dict_1 == dict_2)

#Problem 3
import calculator as cal
def prob_3(a,b):
    a_sq=cal.product(a,a)
    b_sq=cal.product(b,b)
    c=cal.root(cal.plus(a_sq,b_sq))
    return c

#Problem 4
import sys
import random
import box as b
if len(sys.argv) != 2:
    name = input("What is your name? ")
else:
    name = str(sys.argv[1])
A = list(range(1,10))
roll = random.randint(2,12)
while b.isvalid(roll, A) == True and sum(A)!= 0:
    if sum(A)>=6:
        roll = random.randint(2,12)
    else:
        roll = random.randint(1,6)
    print('Numbers Left: {}'.format(A))
    print('Roll: {}'.format(roll))
    player_input = input("Numbers to eliminate: ")
    choice = b.parse_input(player_input, A)
    while sum(choice) != roll and b.isvalid(roll, A)==True:
        print("Invalid input")
        player_input = input("Numbers to eliminate: ")
        choice = b.parse_input(player_input, A)
    else:
        A = [x for x in A if x not in choice]
    point = str(sum(A))
    if sum(A)>=6:
        roll = random.randint(2,12)
    else:
        roll = random.randint(1,6)
if point == "0":
    print('Score for player {}: {} points'.format(name, point))
    print("Congratulations! You shut the box")
else:
    print("Roll: {}".format(roll))
    print("Game over!")
    print('Score for player {}: {} points'.format(name, point))
