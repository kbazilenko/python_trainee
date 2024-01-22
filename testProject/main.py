# вводится число целове, необходимо разбить на десятки и записать их в массив и вывести массив
def splitOfNumber(number):
    digits = []
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    digits = digits[::-1]
    return digits


print(splitOfNumber(112))
