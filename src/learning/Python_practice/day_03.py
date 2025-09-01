# if 문

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

필기 = True
실기 = False
if 필기 and 실기:
    print("합격")
else:
    print("불합격")
        
못생김 = False
돈없음 = False 
키작음 = True
if not 키작음 or 못생김 and 돈없음:
    print("결혼상대자 불합격")
else: 
    print("결혼상대자 합격")


print(1 in [1,2,3])
print(1 not in [1,2,3])
print("a" in ("a","b","c"))
print("j" not in 'python')

pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

여자결혼상대자 = ['못생김','돈없음','작은키']
if '작은키' not in 여자결혼상대자:
    print('결혼생각있다')
else:
    print('혼자살고말지')

pocket = ['card', 'cellphone', 'paper']
if "card" in pocket:
    print("버스를 타고 가라")
else:
    print("걸어가라")

if "money" in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket1 = ['paper','cellphone']
card = False
cellphone = True
if 'money' in pocket1:
    print("택시를 타고 가라")
elif card:
    print("동생에게 전화 해라")
elif cellphone:
    print("동생에게 전화해서 돈가지고 나오라 해라")
else:
    print("걸어가라")

if 'money' in pocket: pass
else: print("카드를 꺼내라")

score = 90
if score >= 60:
    message = "Success!"
else:
    message = "Failure"

# while문

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number =0
while number != 4:
    print(prompt)
    number = int(input())

a=0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

a=0
while a < 10:
    a=a+1
    if a % 3 == 0: continue
    print(a)

#while True:
#    print("Ctrl+C를 눌러야 while문을 빠져 나갈 수 있습니다.")

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