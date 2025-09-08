# if문

age = 20
if age >= 18:
    print('성인')
else:
    print('미성년자')

# for문

for i in [1,2,3]:
    print(i)

# while
n = 0
while n < 3:
    print(n)
    n += 1

arr = [10, 20, 30]
d = {"a":1, "b":2}
print(arr[0],d["a"])

# 1번
age = 15
if age >= 18:
    print('성인')
else:
    print('미성년자')

for i in [1,2,3,4,5]:
    print(i)

# 2번
n = 0
while n < 3:
    print(n)
    n += 1

# 3번
arr = [10,20,30]
d = {"a":1, "b":2}
print(arr[1],d["b"])

#1번
age = 12
if age >= 20:
    print('성인')
elif age >= 13:
    print('청소년')
else:
    print('어린이')
#2번
for i in [2,4,6,8,10]:
    print(i**2)
n = 1

#3번
while n < 11:
    print(n)
    n += 1

#4번
a = [3, 7, 12 ,15, 20]
for b in a:
    print(b % 2)

#5번
prices = {"apple": 1200, "banana": 800, "pear": 1500}
print(prices["banana"])
prices["orange"]=1000
print(prices)