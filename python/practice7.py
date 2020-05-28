#퀴즈5
#난 Cocoa 서비스를 이용하느 택시기사다.
#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
# 조건1 : 승객별 운행 소요 시간은 5~10분 사이의 난수
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 함
from random import *
count=0
for num in range(1,51):
    ran = randint(5,50)
    if(5<=ran<=15):
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(num,ran))
        count+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(num,ran))
print("총 탑승 승객 : {0} 분".format(count))