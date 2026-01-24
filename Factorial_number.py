from math import factorial

number = int(input("Enter the number:"))
def fact_num(number):
    # base condition
    if number == 1:
        return 1
    else:
        factorial = number * fact_num(number-1)
        return factorial
print(f"Factorial of a {number} is {fact_num(number)}")
