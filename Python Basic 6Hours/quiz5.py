#퀴즈5
#난 Cocoa 서비스를 이용하느 택시기사다.
#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
# 조건1 : 승객별 운행 소요 시간은 5~10분 사이의 난수
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 함
from random import *
for num in range(51):
    ran = randint(5,50)
    print("[{0}] {1}번째 손님 (소요시간 : {2}분".format(num,num+1,ran))
    if(5<=ran and ran<=15):
        count+=1
print("총 탑승 승객 : {0} 분".format(count))