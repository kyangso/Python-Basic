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

def mt(m, n):
    return m * n / 2

print(mt(10, 20))
