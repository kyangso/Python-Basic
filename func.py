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


def say(name):
    print(name, "님이 입장하셨습니다 ")     # 파라미터는 코드 안에사용되는거 


say("park")
say("kim")
say("choi")
say("yang")
say("lee")
say("gang")
say("jo")