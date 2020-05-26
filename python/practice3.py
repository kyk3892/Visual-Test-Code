#문자열
print("문자열 예제")
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" #약간 pre태그처럼 나옴
print(sentence3)

#슬라이싱
print("슬라이싱 예제")
jumin = "010219-1234567"
print("성별 : "+jumin[7])
print("연 : "+jumin[0:2]) #0~2 직전까지 0,1번째 값 가져옴
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6]) #처음부터 6직전까지
print("주민번호 뒷자리 : "+jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에부터) : "+jumin[-7:]) #맨뒤에서부터 7번째 끝까지

#문자열처리함수
print("문자열 처리함수 예제")
python = "Python is Amazing"
print(python.lower()) #모두 다 소문자
print(python.upper()) #모두 다 대문자
print(python[0].isupper()) #이 0번째가 대문자인가?
print(len(python)) #python의 길이 출력
print(python.replace("Python", "Java")) #Python단어를 찾아서 Java로 바꾸기

index = python.index("n")
print(index)
index = python.index("n", index+1) #첫번째 n뒤 다음 n이 있는 자리
print(index)

print(python.find("Java")) #-1이 나옴
# print(python.index("Java")) #오류가 남
print(python.count("n")) #n이 총 몇번 등장하는가

#문자열 포맷1
print("문자열 포맷1")
print("나는 %d살입니다." %20) # %d d는 정수값만
print("나는 %s을 좋아해요" %"파이썬") # %s는 문자열, 숫자나 문자도 가능함
print("Apple은 %c로 시작해요" %"A") # %c는 문자
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨강"))

#문자열 포맷2
print("문자열 포맷2")
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요" .format("빨강", "노랑"))

#문자열 포맷3
print("문자열 포맷3")
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))

#문자열 포맷4
print("문자열 포맷4")
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #앞에 f붙이면 위에 선언한 값 사용가능

#탈출 문자
print("탈출문자")
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견 \n백견이 불여일타")
print("저는 \"김윤희\"입니다.")
print("Red Apple\rPine") #\r : 커서를 맨 앞으로 이동
print("Redd\bApple") #\b : 한 글자 삭제
print("Red \t Apple")

#퀴즈3
#사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
#예)http://www.naver.com
#규칙1 : http://www. 부분은 제외 -> naver.com
#규칙2 : 처음 만나는 점 이후 부분은 제외 -> naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
site = "http://www.naver.com"
num1 = site[-9:]
num2 = num1[:num1.index(".")] #num1중에서 .이전까지 자름
num3 = num2[0:3]
strc = len(num3)
enum = site.count("e")
print("생성된 비밀번호 : "+str(num3)+str(strc)+str(enum)+"!")