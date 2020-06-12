#연산자
print("연산자")
print(2**3) #2의 3제곱
print((3>0) and (3<5))
print((3>0) & (3<5))
print((3>0) or (3>5))
print((3>0) | (3<5))
print(5>4>3) #True
print((5>3>7)) #False

print(abs(-5)) #abs는 절댓값
print(pow(4,2)) #4의 2제곱
print(max(5,12)) #max는 최댓값 12
print(min(5,12)) #min은 최솟값 5
print(round(3.14)) #round는 반올림

from math import *
print(floor(4.99)) #floor는 내림
print(ceil(3.14)) #ceil은 올림
print(sqrt(16)) #sqrt은 제곱근

from random import *
print(random()) #0.0~1.0까지 수
print(random()*10)
print(int(random()*10)) #0~10까지 임의의 정수값
print(int(random()*10)+1) #0을 제외한 10까지의 정수값

print(randrange(1,46)) #1~46미만의 임의의 값 생성
print(randint(1,45)) #1~45까지 임의의 값 생성