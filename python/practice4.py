#리스트[]
#지하철 칸별로 10명, 20명, 30명
#3개의 서로 다른 변수
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10,20,30] #리스트 만들기
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
#리스트 추가하기
subway.append("하하")
print(subway)

#정형돈씨를 유재석/조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() #순서대로 정렬
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#리스트 안에 있는 모든 요소 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
print("리스트 확장")
num_list.extend(mix_list)
print(num_list)

#사전 딕셔너리
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) #키 값 가져오기
print(cabinet.get(5, "사용 가능")) #값이 없기 때문에 사용 가능이란 값을 줌

#3이란 키가 cabinet안에 있는가
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#호텔 폐점
cabinet.clear()
print(cabinet)