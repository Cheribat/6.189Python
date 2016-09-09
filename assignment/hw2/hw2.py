# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math
import random

# **********  Exercise 2.0 ********** 

def f1(x):
    print (x + 1)

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

print("Exercise 2.1 has been finished.")

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
def is_divisible (m, n):
    if(n != 0):
        if(m % n == 0):
            return True
        else:
            return False
    else:
        return False

# Test cases for is_divisible
print(is_divisible(9, 3))
print(is_divisible(5, 2))
print(is_divisible(0, 2))
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5))  # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 0))  # What should this return?


# Define not_equal function here
def not_equal(m, n):
    if(m == n):
        return False
    else:
        return True

# Test cases for not_equal
print(not_equal('a', 8))
print(not_equal("TH", "TH"))
print(not_equal(15, 15))
print(not_equal(12, 54))


# ********** Exercise 2.3 ********** 
## 1 - multadd function
def multadd(a, b, c):
    return (a * b + c)

## 2 - Equations
# Test Cases
angle_test = multadd(1/2, math.cos(math.pi/4), math.sin(math.pi/4))
print ("sin(pi/4) + cos(pi/4)/2 is:")
print (angle_test)

ceiling_test = multadd(2, math.log(12, 7), math.ceil(276/19))
print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)

## 3 - yikes function
def yikes (x):
    return(multadd(x, math.exp(-x), math.sqrt(1 - math.exp(-x))))


# Test Cases
x = 5
print ("yikes(5) =", yikes(x))

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
def rand_divis_3 ():
    return(random.randint(0, 100) % 3 == 0)

# Test Cases
print(rand_divis_3())

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(num, cnt):
    for i in range (cnt):
        print(random.randint(1, num))
    print("That's all!")

# Test Cases
roll_dice(6, 10)                          


# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
    delta = b * b - 4 * a * c

    if (delta >= 0):
        root1 = -b / (2 * a) + math.sqrt(delta)
        root2 = -b / (2 * a) - math.sqrt(delta)
    else:
        root1 = complex(-b / (2 * a)+math.sqrt(-delta)*1j)
        root2 = complex(-b / (2 * a)-math.sqrt(-delta)*1j)

    return (root1, root2)
        

# Test Cases
print(roots(1, 2, 3))
print(roots(1, 2, 1))
print(roots(1, 3, 3))
