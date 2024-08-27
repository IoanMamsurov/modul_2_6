def password(number):
    password = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


print('Введите число: ')
print(password(int(input())))
