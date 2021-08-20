def fizz_buzz(max):

    numbers = []

    for x in range(0, max):
        if((x % 4 == 0 or x % 6 == 0) and (x % 4 != 0 or x % 6 != 0)):
            numbers.append(x)

            x += 1
            
    return numbers
print(fizz_buzz(30))

