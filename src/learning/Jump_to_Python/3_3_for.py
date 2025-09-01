#for 문

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2),(4,5),(7,8)]
for (first,second) in a:
     print(first+second)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark > 60:
        print('%s번 학생은 합격입니다.' % number)
    else:
        print('%s번 학생은 불합격입니다.' % number)

for mark in marks:
    number = number + 1
    if mark > 60:
        print("%s번 학생 축하합니다. 합격입니다." % number)
    elif mark < 60:
        print("%s번 학생 죄송합니다. 불합격입니다." % number)
        continue

a = range(10)
print(a)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

marks = [90,25,65,80,55]
number = 0
for number in range(len(marks)):
    if marks[number] > 60:
        print("%s번 학생 축하합니다. 합격입니다." % number)
    elif marks[number] < 60:
        print("%s번 학생 안타깝지만 불합격입니다." % number)
        continue
    
add = 0
for p in range(0,101):
    add = add + p

print(add)

gugu = 0
for G in range(2,10):
    gugu = G * (gugu+1)

print(gugu)