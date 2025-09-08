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
