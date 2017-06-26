# test_solutions.py
"""Testing
Sophia Mo
06/26/2017
"""

import solutions as soln
import pytest
import math

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,3) == 4
    assert soln.addition(-1,-3) == -4
    assert soln.addition(1,-5) == -4

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1
    assert soln.smallest_factor(5) == 5
    assert soln.smallest_factor(4) == 2

# Problem 2: Test the operator function from solutions.py
def test_operator():
    assert soln.operator(1,3,"+")==4
    assert soln.operator(1,3,"/")==1/3
    assert soln.operator(1,3,"-")==-2
    assert soln.operator(1,3,"*")==3
    with pytest.raises(Exception) as excinfo:
        soln.operator(1,1,1)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be a string"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1,1,"++")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be one character"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1,0,"/")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "You can't divide by zero!"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1,1,"#")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_sub(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3, -4)

def test_complex_div(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber.__div__(number_1 , number_2) == soln.ComplexNumber(0.3, 0.1)
    assert soln.ComplexNumber.__div__(number_1 , number_3) == soln.ComplexNumber(4/17, -1/17)
    assert soln.ComplexNumber.__div__(number_2 , number_3) == soln.ComplexNumber(11/17, -7/17)
    with pytest.raises(Exception) as excinfo:
        soln.ComplexNumber.__div__(number_1 , 0)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Cannot divide by zero"

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber.conjugate(number_1) == soln.ComplexNumber(1, -2)
    assert soln.ComplexNumber.conjugate(number_2) == soln.ComplexNumber(5, -5)
    assert soln.ComplexNumber.conjugate(number_3) == soln.ComplexNumber(2, -9)

def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber.norm(number_1) == math.sqrt(5)
    assert soln.ComplexNumber.norm(number_2) == math.sqrt(50)
    assert soln.ComplexNumber.norm(number_3) == math.sqrt(85)

def test_complex_eq(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber.__eq__(number_1, number_2) == False
    assert soln.ComplexNumber.__eq__(number_1, number_1) == True

def test_complex_str(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber.__str__(number_1) == "1+2i"
    assert soln.ComplexNumber.__str__(number_2) == "5+5i"
    assert soln.ComplexNumber.__str__(number_3) == "2+9i"

# Problem 4: Write test cases for the Set game.
def set_up_sets():
    with open('set1.txt', 'r') as myfile:
        set1 = [int(i) for i in myfile.read().split('\n')]
    with open('set2.txt', 'r') as myfile:
        set2 = [int(i) for i in myfile.read().split('\n')]
    with open('set3.txt', 'r') as myfile:
        set3 = [int(i) for i in myfile.read().split('\n')]
    with open('set4.txt', 'r') as myfile:
        set4 = [int(i) for i in myfile.read().split('\n')]
    with open('set5.txt', 'r') as myfile:
        set5 = [int(i) for i in myfile.read().split('\n')]
    return set1, set2, set3, set4, set5

def test_set(set_up_sets):
    set1, set2, set3, set4, set5 = set_up_sets
    assert soln.set(set1) == 6

    with pytest.raises(Exception) as excinfo:
        soln.set(set2)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Should have 12 cards"

    with pytest.raises(Exception) as excinfo:
        soln.set(set3)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Should not have duplicate cards"

    with pytest.raises(Exception) as excinfo:
        soln.set(set4)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Input is invalid"

    with pytest.raises(Exception) as excinfo:
        soln.set(set5)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Wrong file name"
