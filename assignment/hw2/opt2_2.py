# author    : Will Fu
# date      : 2016-09-09

num1 = [(x, y) for x in range(-5, 6)  for y in range (0, 11)]
num2 = [(x, y) for (x, y) in num1 if y == x**2 + 1]
print(num2)
