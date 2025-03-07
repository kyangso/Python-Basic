# 변수(variable)
# 변수(variable) = 값
# 위 형식으로 변수(variable)에 값을 저장
# = 기호의 뜻과 다르게 단순하게 값이 변수(variable)에 저장
# 1. 숫자로 시작 불가능
# 2. 기호 "_"를 제외한 특수문자 불가능
# 3. 띄어쓰기 불가능
# 4. 예약어 불가능

# my_name = "WONJAE"


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 자료형(Data type)
# str   -> String           문자    => 따옴표로 이루어져 있음(따옴표가 있으면 무조건 문자) " " ' '
# float -> Float            실수    => 따옴표가 없고 소수점이 있으면 실수
# int   -> Integer          정수    => 따옴표가 없고 소수점도 없으면 정수
# 일상적으로 사용하는 말들 (영어, 중국어, 한국어 등)이 따옴표가 없다 => ERROR

# a = 10      # a라는 변수에 int 자료형인 10 저장
# b = 'cit'   # b라는 변수에 str 자료형인 'cit' 저장


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('문자' or 변수 or 숫자)
# print('문자' or 변수 or 숫자) 함수는 괄호안에 있는 '문자', 숫자 또는 변수의 값을 출력한 후 엔터한다.
# 한줄에 여러개를 출력하고 싶으면 콤마(,)를 사용
# 만약 print()를 사용할 경우 빈 한줄이 출력

# name = '파이썬'
# age = 28
# height = 188
# print(name)
# print()         # 빈 한줄 출력
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 자료형을 확인하는 방법
# type() => 괄호안에 있는 변수 또는 값의 자료형을 가지고 옴
# type(변수)        <= 이런식으로 사용하는 경우 프로그램으로 동작은 하지만 자료형을 눈으로 볼수 없음
# print(type(변수))
# 위 형식으로 print()안에 넣어서 주로 사용

# int0 = 1            # int0라는 변수에 int 자료형인 1을 저장
# float0 = 3.14
# str0 = 'test'
# type(int0)          # 동작을 하지만 자료형을 눈으로 볼 수 없음
# print(type(int0))   # type()을 사용하여 int0의 자료형 출력
# print(type(float0))
# print(type(str0))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 형 변환(casting)
# str(변수 or 값)   => 변수 or 값을 str 자료형으로 변환
# float(변수 or 값) => 변수 or 값을 float 자료형으로 변환
# int(변수 or 값)   => 변수 or 값을 int 자료형으로 변환
# 단순히 연산할때만 사용하면 원본의 값은 변하지 않음
#원본의 자료형을 변환 시키기 위해서는 변수에 값을 다시 넣어야 함 [ ex. a = int(a) ]

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # result 변수에 var1 변수 + int 자료형으로 변환한 var2 변수 저장
# print(result)
# print(type(var2))           # 변수 var2 자료형을 출력, result 변수에는 int 자료형으로 계산이 되었지만
#                             # 실제 변수의 자료형은 변환 안됨
# var2 = int(var2)            # var2 변수에 int 자료형으로 변환한 var2 변수 저장
# print(type(var2))           # 변수 var2 자료형을 출력


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input('문자' or 변수)
# '문자' 또는 변수를 출력한 후 엔터키를 누르기 전까지 키보드 입력을 받음
# '문자' 또는 변수는 생략 가능
# 변수 = input('문자' or 변수)
# 위 형식을 주로 사용, input()만 사용했을 경우 입력 값을 저장하지 못함
# input()은 무조건 str 자료형으로 값을 저장함

# var1 = 2
# var2 = input("Insert anything : ")
# print(var2)
# print(type(var2))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('안녕하세요.이름을 입력해주세요')
# name = input()

# print('환영합니다.', name, '님. 나이를 입력해주세요.')      # 여러개를 입력할때엔 print()하나에 넣지 않고 콤마(,)를 쓴다.
# age = input()
# year = 2024
# age = int(age)          # int(age)만 적으면 *그 줄*만 저장되고 나머진 똑같기에 저장할떄엔 꼭 (문자 or 변수) = (int or str or float)(문자 or 변수)를 해야한다.

# print(year - age, '년에 태어나셨군요! 키를 입력해주세요.') 
# height = int(input())   # input()을 int()에 묶어두면 입력받자마자 숫자로 변경
# print('2m까지', 200 - height, 'cm 남으셨네요.')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('본인의 키는?')
# height = int(input())       # input()을 int()에 묶어두면 입력받자마자 숫자로 변경

# print('좋아하는 숫자는?')
# like_number = int(input())  # input()을 int()에 묶어두면 입력받자마자 숫자로 변경

# print('키와 좋아하는 숫자의 합은', height + like_number, '입니다.')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# +     더하기
# -     빼기
# *     곱하기
# /     나누기(소수로 나옴)
# //    몫(정수로 나옴)
# %     나머지
# **    제곱

a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)