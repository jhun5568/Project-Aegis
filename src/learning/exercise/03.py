def solution(str):
    a = ""  #문자를 담기 위한 빈그릇을 준비한다.
    for ch in str: # str(입력문자)를 확인해서 ch를 하나씩 꺼낸다
        if ch.isupper(): # ch가 대문자이면
            a = a + ch.lower() #소문자로 바꿔서 a로 붙이고.
        else: # 그 외에는(ch가 소문자이면)
            a = a + ch.upper() #대문자로 바꿔서 a에 붙여라.
    return a # 변환이 끝나면 a 반환.

print(solution("aBcDeF")) # 입력 값을 출력해라

