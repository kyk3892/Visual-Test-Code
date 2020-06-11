#튜플은 리스트와 다르게 내용변경이나 추가를 할 수가 없음
menu = ("신전떡볶이", "치즈떡볶이")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name,age,hobby)

#세트(집합)
#중복 안됨, 순서 없음
my_set = {1,3,4,3,3}
print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) #유재석 둘 다 겹침

#교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) #2가지 방법 모두 사용 가능

#합집합(java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합(java는 할 수 있지만 python은 할 수 없는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(java)

#java를 까먹음
java.remove("김태호")
print(java)

#자료 구조의 변경

menu = {"커피", "우유", "쥬스"} #기본 타입 set임 대괄호 사용
print(menu, type(menu))

menu = list(menu) #타입 list로 변경 중괄호 사용
print(menu, type(menu))

menu = tuple(menu) #타입 tuple로 변경 소괄호 사용
print(menu, type(menu))

menu = set(menu) #타입 set으로 바꾸기
print(menu, type(menu))