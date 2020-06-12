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