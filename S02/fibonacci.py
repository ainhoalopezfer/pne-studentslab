n1, n2, count = 0, 1, 0

while count < 11:
    nth = n1 + n2
    print(n1, end=" ")

    n1, n2 = n2, nth
    count += 1

