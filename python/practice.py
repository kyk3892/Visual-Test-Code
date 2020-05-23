#python 자료형
print('풍선')
print("나비")
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)

#애완동물을 소개해주세요~
animal = "강아지"
name = "호두와 마루"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"에요")
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요") #age와 같은 숫자를 ++안에 사용하기 위해서는 str로 바꿔줘야함 str(age)
print(name+"는 어른일까요? "+str(is_adult)) #boolean형도 str로 감싸줘야함
print(name,"는 ", age,"살이며, ",hobby,"을 아주 좋아해요") #+대신 , 사용 가능 하지만 띄어쓰기 추가됨

#주석 python의 주석은 #, '''이렇게 하면 여러 문장이 주석처리''', 단축키 ctrl+/

#퀴즈
#Quiz) 변수를 이용하여 다음 문장을 출력하시오
station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")