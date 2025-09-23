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