print("Hello world")
print("This is my first Python program")
print("Life is too short!")
print("Life is too short!".replace("Life", "Your legs"))
print("I love Python".replace("love", "like"))
print("1 + 1 =", 1 + 1)
name = '배성준'
age = 47
print(f"나의 이름은 {name} 이고 나이는 {age} 입니다. 내년이면 {age + 1} 살이 됩니다.")
print(len("나의 이름은 {name} 이고 나이는 {age} 입니다. 내년이면 {age + 1} 살이 됩니다."))
a = 10
b = 20
print(f"{a} + {b} =", a + b)

#list
a = [1, 2, 3]
print('a[0] =',a[0])
print('a[0] + a[2]',a[0] + a[2])
print('a[-1]',a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][0])  # 'a'
print(a[3][1])  # 'b'
print(a[3][2])  # 
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(a[0:2])  # [1, 2]
print(a[:2])   # [1, 2]
print(a[1:3])  # [2, 3]
print(a[1:])   # [2, 3, 4, 5]
print(a[1:2])  # [2]
print(a[2:])   # [3, 4, 5]
print(a+b)
print(len(a))
print(len(a+b))
a[3] = 8
print(a)
del a[2]
print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.insert(3, 13)
print(a)
a.remove(1) # 1 제거
print(a)
a.pop() # 마지막 요소 제거
print(a)
a.pop(0)
print(a)

#튜플
a1 = ()
a2 = (1)
a3 = (1, 2, 3)
a4 = 1, 2, 3
a5 = ('a', 'b', ('ab', 'cd'))
print(a1, a2, a3, a4, a5)

#딕셔너리
a = {'name': '이한나', 'phone': '010-1234-5678', 'birth': '1914-06-01'}
print(a['name'])

dic = {'name': '홍길동', 'birth': 1128, 'age': 30}
print(dic)

a = {'국어': 80, '영어': 75, '수학': 55}
print((80+75+55)/3)
#홀수

print(1 % 2)

pin="881120-1068234"
print("19"+pin[:6])
print(pin[7:])

print(pin[7])

a='a:b:c:d'
b=(a.replace(':', '#'))
print(b)

a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a=['life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)  

a = (1, 2, 3)
a = a + (4,)
print(a)

a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
a[1] = 'python'
a[250] = 'python'
print(a)

a= {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

a=b=[1,2,3]
a[1]=4
print(b)


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")