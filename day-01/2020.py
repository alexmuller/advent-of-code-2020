f = open('expenses.txt')

numbers = [int(x) for x in f.read().split("\n") if x != ""]

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            result = int(num1) + int(num2) + int(num3)
            if result == 2020:
                print num1, num2, num3
                print num1*num2*num3
