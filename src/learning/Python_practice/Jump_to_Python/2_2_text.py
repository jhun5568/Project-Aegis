print("Hello World")
print('Python is fun')
food = "Python's favorite food is perl"
print(food)
print('"Python is very easy. He says"')
say = '"Python is very easy. He says"'
print(say)
print('''Life is too short
You need python''')
print(say[:6]+"is very hard"+say[20:])
print("=" * 50)
print("My Program")
print("=" * 50)
print(10*18**2+2*11)
a=5
b=6
print("%s / %s 몫과 나머지는?" %(a, b))
print("몫=",a // b)
print("나머지=",a % b)
print("I ate {0} apples. So I sick {1} days".format(a,b))
print("'{0:=^10}'".format("hi"))
y=3.15345612468
print("{0:0.4f}".format(y))

#아래는 파이썬 3.6 이상 버전에만 적용가능함.
name = "이한나"
age = 35
print(f"나의 이름은 {name}입니다. 나이는 {age} 입니다.")
print(f"나는 내년이면 {age+1}살이 된다")
d={'name':'배성준','age':'47'}
print(f"나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]}입니다.")
print(f'{"Hi":<10}')
print(f'{"Hi":>10}')
print(f'{"Hi":^10}')
print(f'난 {1500000000:,}원이 필요해')

#count 해당 문자 갯수
a = 'hobby'
b = 'table tennis'
print(a.count('b'))
print(b.count('t'))
#find 해당 문자 순번 알려주기
c = 'Python is the best choice'
print(c.find('b'))

print(f"My {a} is {b}.")

#index 해당 문자 순번 알려주기(없을 시 오류 메세지)
a="Life is short."
print(f"{a}""index'T'=",a.index('t'))

#join 문자열 삽입
print(','.join('abcd'))
