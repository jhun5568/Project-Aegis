from random import *
print(random())
print(randint(1,45))


python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Jave"))

index = python.index("n") #위치
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java")) #-1 원하는 값이 없을 때 -1 반환
# print(python.index("Java")) #오류 발생
print("hi")
print(python.count('n'))
