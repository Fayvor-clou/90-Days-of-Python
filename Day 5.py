#Write a function that takes a number as input and returns the factorial of that number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 10
print(f"The factorial of {number} is {factorial(number)}")
