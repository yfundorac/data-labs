# def my_function(X):
#     solutions = []
#     for x in range(5, X): #hipotenusa
#         for y in range(4, X):
#             for z in range(3, X):
#                 if (x*x==y*y+z*z):
#                   solutions.append([x, y, z])
#     m = 0
#     for solution in solutions:
#         if m < max(solution):
#             m = max(solution)
#     return m

# X = input("What is the maximal length of the triangle side? Enter a number: ")

# print("The longest side possible is " + str(my_function(int(X))))

"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""


def longest_side(x):
    X = x + 1
    return max([
        c 
        for c in range(5, X) 
        for b in range(4, X) 
        for a in range(3, X) 
        if (a ** 2 + b ** 2 == 
            c ** 2)
    ])


# X = input("What is the maximal length of the triangle side? Enter a number: ")

# print("The longest side possible is " + str(longest_side(int(X))))

print(longest_side(15))


# Bonus - David's code
# https://codereview.stackexchange.com/questions/153542/finding-integer-lengths-for-a-right-triangle-with-a-given-perimeter/153547cd 

def hypotenuse(X):
    p = X * 3 # Max perimeter
    for b in range(1, p // 2):
        a = ((2 * b * p) - p ** 2) / (2 * (b - p))
        if int(a) == a: # Whole numbers only
            yield max(a, b, p - a - b)

def euler(X):
    return max([j for i in range(X) for j in hypotenuse(i) if j < X])

print(euler(300))
