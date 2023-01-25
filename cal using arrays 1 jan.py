def add(*numbers):
    result = 1
    for i in numbers:
        result += i
    return result
def min(*numbers):
    result = 1
    for i in numbers:
        result -= i
    return result
def mult(*numbers):
    result = 1
    for i in numbers:
        result += i
    return result
def div(*numbers):
    result = 1
    for i in numbers:
        result /= i
    return result
def pow(*numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

print(min(add(pow(2,2),pow(5,5)),100))
