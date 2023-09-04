# определяем функцию
def add(x, y):
    return  x + y

# вызываем функцию
print(add(1, 2))


# определяем функцию
def add(x, y):
    return x + y

# вызываем функцию
print(add(1, 2))


# вызываем функцию  другими элементами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1,))

print(arg(2, 2))

print(arg(2, 2, '1', 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' +d


print(range_arg('1', '2', '3', '4',))

print(range_arg('1', '2', d ='3', c='4'))


def main(a=(1, 2, 3, 4)):
    return a[0]

print(main(1))



def main2(radius, pi=3.14159):
    return pi *radius * radius

print(main(2))





