def doubler(number):
    doubled_num = []

    for x in range (len(number)):
        doubled_num.append(number[x]*2)

    return doubled_num
print(doubler(number=[2,4,6]))
