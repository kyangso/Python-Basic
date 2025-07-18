# 함수(function)
# 함수란 어떤 기능을 하는 것으로 크게 이미 있는 함수와 직접 만든 함수가 있다.

# def funtion_name(parament):
#       (코드넣는자리..)
#       return  (값)or(변수)

# 위형식으로함수를직접만들 '수' 있으며 만든함수실행의경우아래와같음
# funtion_name(arguement)
#          
# parameter ----> 함수 내부에서 사용하는 변수
# return -------> 함수를 종료하며, 특정 값을 함수를 실행한 곳으로 돌려줄 수 있음
# arguement ----> 함수를 실행할때 넘겨주는 값
# parameter, return, arguement는 필수가 아님
# 함수가 정의할때 parameter의 개수와 함수를 실행할때의 arguement의 개수는 같아야 함

# def a():                 # parameter, return 이 없는 경우
#     print("Hello")

# def b(name):             # return이 없는 경우
#     print(name, "Hi")

# def c(a):
#     return a+10

# a()
# b("Jeong")
# var = c(5)              # 보통 return이 있는 함수의 경우 변수랑 같이 사용
# print(var)
# b(var)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def welcome(name):
#     print("Hello!", name)
#     return "Bye."

# welcome("최원재")
# re = welcome("Bye.")
# print(re)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def say(name):
#     print(name, "님이 입장하셨습니다 ")     # 파라미터는 코드 안에사용되는거 


# say("park")
# say("kim")
# say("choi")
# say("yang")
# say("lee")
# say("gang")
# say("jo")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(num):
#     print("*" * num)


# for i in range(1, 10, 1):
#     star(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 함수를 선언(정의), return을 사용한 경우
# def bmi_return(weight, height):
#     BMI = weight / height / height


#     return BMI

# return 없이 함수를 선언
# def bmi_no_return(weight, height):
#     BMI = weight / height / height

#     print(BMI)

# 함수를 호출(실행)
# print(bmi_return(67,  1.78))
# bmi_no_return(67, 1.78)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# return의 경우 보통 함수끼리 서로 값을 공유할때 사용

# def check_score(score):     # 점수들 중 50점 이상의 점수를 구분하여 리스트로 리턴
#     over = []
#     for i in score:
#         if(i >= 50):
#             over.append(i)

#     return over

# def average(score):         #평균을 구함
#     print(sum(score) / len(score))


# score = [51, 99, 78, 34, 75, 22, 12]
# over_50 = check_score(score)    # check_score 함수를 통해서 50점 이상인 점수를 over_50에 저장
# print(over_50)
# average(over_50)                # 50점 이상인 점수의 평균을 구함


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 거리와 시간을 입력으로 받아 속도를 출력하는 함수

# def speed(d, t):
#     speed = d / t
#     return speed

# print(speed(10, 10))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 밑변과 높이를 입력으로 받아 삼각형의 넓이를 출력하는 함수

# def mt(m, n):
#     return m * n / 2

# print(mt(10, 20))


# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("A")
# print("B")
# abc = input("다음이 뭐였지..?  대답 :")
# if(abc == "C"):
#     print("right!맞았어!")
# elif(abc == "c"):
#     print("right!맞았어")
# else:
#     ("틀렸어.. 이걸 몰라?다시공부해 ")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# **     *      공백 : 5개
# * *    *      별 기준 왼쪽 : 공백 1개 , 별 기준 오른쪽 : 공백 4개
# *  *   *      별 기준 왼쪽 : 공백 2개 , 별 기준 오른쪽 : 공백 3개
# *   *  *      별 기준 왼쪽 : 공백 3개 , 별 기준 오른쪽 : 공백 2개
# *    * *      별 기준 왼쪽 : 공백 4개 , 별 기준 오른쪽 : 공백 1개
# *     **      별 기준 왼쪽 : 공백 5개 , 별 기준 오른쪽 : 공백 0개


# def star(n):                                            # 문제 이해하기(!가장 중요한것!)
#     blank = ' '
#     print("*%s*%s*" % (blank*n, blank*(5-n)))           #포멧팅 활용하기

# for i in range(0, 6, 1):
#     star(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 변수는 크게 local, global 두가지가 있음
# local 변수    : 함수 내부에서 만들었고 함수 내부에서만 쓰이는 변수
# global 변수   : 함수 밖에서 만들었고 함수 내외부 둘다 사용 가능
# 변수의 이름과 local, global은 상관 없으며, 변수는 기본적으로 global 변수를 얘기함

# a = 10      # global 변수

# def test():
#     a = 5       # local 변수
#     b = 20      # local 변수

# print(a)
# test()
# print(a)        # test 함수를 실행해도 a 값은 변화가 없음
# print(b)         # 변수 b는 test 함수에서만 사용하기 때문에 함수 밖에서 참조를 하는 경우 에러 발생


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 함수  밖에    있는    변수의  값을    함수 내부에서 변경하    는법법
# global 변수
# 위 형식으로 함수 내부에서 함수 밖에 있는 변   수의 값을 변경할 수 있음음
# glo   bal을 사용 안해도 함수 내qn에서 값을 참조는 가능하지만 값   변경은 불가능능

# bmi = 0

# def BMI(height, weight):
#     global bmi
# global bmi = 0
#     height = height / 100
#     bmi = weight / (height*height)

#     return bmi

# print(bmi)
# print(BMI(178, 80))
# print(bmi)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 재귀함수
# 함수 내부에서 자기자신을 호출하는 함수
# def function():
#       print('Hello')
#       input()
#       function()           # 자기 자신을 호출

# function()

# 피보나치 수
# https://pythontutor.com/render.html#mode=display
# def fibonacci(a,b):
#     c = a + b
#     if(a < 100):
#         print(a,end='  ')
#         return fibonacci(b, c)  # return None이 계속 반복되어서 호출한 함수들이 종료된다
#     else:
#         return                  # return하는 값 또는 변수가 없기 때문에 NoNe이 return됨
    
# fibonacci(1, 1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


