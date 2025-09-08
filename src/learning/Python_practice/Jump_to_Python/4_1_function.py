def add(a,b):
    return a+b
a = 3
b = 4
c = add(a,b)
print(c)

def add(a,b):
    result = a + b
    return result
sum = add(5,6)
print(sum)

def say():
    return 'Hi'
a = say()
print(a)

def sub(a, b):
    return a - b

result = sub(7, 3)
print(result)

result = sub(b=5, a=3)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(result)

#추가 복습 2025-09-02

#출력이 없는 함수
def sum(a,b):
    print("%d와 %d의 합은 %d 입니다." %(a,b,a+b))

sum(1,2)

#출력이 있는 함수
def sum(a,b):
    return "%d와 %d의 합은 %d 입니다." %(a,b,a+b)

a = sum(4,5)
print(a)

#출력값이 없는 함수
a=[1,2,3]
print(a.append(4))

#출력값이 있는 함수
a=[1,2,3]
print(a.pop())

