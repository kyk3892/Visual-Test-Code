#퀴즈4
#파이썬 코딩대회를 통해 1명은 치킨, 3명은 커피 쿠폰
#조건1 : 편의상 댓글을 20명이 작성하였고 아이디는 1~20이라고 가정
#조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건3 : random 모듈의 shuffle과 sample 활용

#shuffle은 값이 마음대로 섞임
#sample은 리스트에서 몇개를 뽑겠다
#print(sample(1st,1)) 예시

#출력 예제
#-- 당첨자 발표 --
# 치킨 당첨자  : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *

users = range(1,21) #1~20까지 숫자를 생성 range를 사용해서 기본 타입이 range가 됨 리스트에서 쓸 수가 없어서 변환해줘야함
users = list(users) #타입 리스트로 바꾸기
shuffle(users)
winners = sample(users,4) #4명 중에서 1명은 치킨, 3명은 음료 쿠폰

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")


