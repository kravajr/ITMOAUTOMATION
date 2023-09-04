a: int = 5
b: str = 'строка'
c: list = [1, 2]



def ident(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + 5


print(indent('123', 123))


def function_1(s: str = '') ->int:
    return len (s)

print (function_1(''))

def function_1(l1, l2):
    print(long(1,2))




