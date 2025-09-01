def add(a,b):
    return a+b
a = 3
b = 4
c = add(a,b)
print(c)

def add(a,b):
    result = a + b
    return result
a = add(a,b)
print(a)

def say():
    return 'Hi'
a = say()
print(a)

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
