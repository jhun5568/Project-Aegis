# 문자열 포맷
# print("a" + "b")
# print("a","b")

# #방법 1
# print("나는 %d살 입니다." % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple은 %c로 시작해요" % "A")

# # %s
# print("나는 %s살 입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

# # 방법 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {color}살이며, {age}색을 좋아해요." .format(age = 20, color = "빨간"))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")      

# # 탈출문자
# print("백문이 불여일견\n백견이 불여일타")
# # 저는 "나도코딩" 입니다.
# print("저는 \"나도코딩\" 입니다.")
# print("저는 \'나도코딩\' 입니다.")

# #\\ : 문장 내에서 \ 하나로 변경
# print("C:\\Users\\JUN\\Desktop\\Auto-CVS-Project>")

# #\r : 커서를 맨 앞으로 이동 
# print("Red Apple \rPine")

# #\b : 백스페이스 (한 글자 삭제)
# print("Red\bApple")

# \t : 탭
# print("Red \tApple")

#사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.compile
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 객수 + 글자 내 'e' 갯수 + "!" 로 구성

# 생성된 비밀번호 : nav51!

url = 'http://nate.com'
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))
