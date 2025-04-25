# string = "cit academy"

# 인덱스 번호를 이용하여 문자열의 하나의 값을 가지고 올수 있음
# print(string[3])
# print(string[4])

# 슬라이싱을 이욘하여 문자열의 일부분의 값을 가지고 올수 있음
# print(string[1:4])  # string 변수의 문자열 인덱스의 1부터 4까지의 값을 가지고 옴(4는 포함 NONO^o^)
# print(string[5:9])  # string 변수의 문자열 인덱스의 5부터 9까지의 값을 가지고 옴(9는 포함 X!^o^)

# 슬라이싱의 숫자를 생략할수 있음.
# 생략을 할경우 처음또는 끝까지 값을 가지고 옴
# print(string[:3])   #string 변수의 문자열 인덱스의 처음부터 3까지의 값을 가지고옴(3은 포함 NONO^ㅇ^)
# print(string[8:])   # string 변수의 문자열 인덱스의 8부터 끝까지의 값을 가지고옴
# print(string[:])    # string 변수의 문자열 인덱스의 처음부터 끝까지의 값을 가지고옴  print(string) 이코드와 같음


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# string0 = 'cit academy'
# print (string0)
# print()

# split (문자열)
# 문자열을 문자열로 나누어 리스트로 리턴
# 만약에 나눌 문자가 없을 경우 해강 문자열 전체를 하나의 리스트로 생성
# print("split('a') :", string0.split('a'))
# print()

# count(문자열)
# 문자열에서 특정 문자열의 개수를 리턴 => 수를 알고 싶은 문자의 길이는 상관없음
# 만약에 문자가 없을경우 0을 리턴
# print( "count('a') :", string0.count('a'))
# print()

# upper()   => 문자를 전부 대문자로
# lower()   => 문자를 전부 소문자로
# print('upper() :', string0.upper())
# print('lower() :', string0.lower())
# print()

# replace(문자1, 문자2)
# 문자1을 문자2로 전부 변경
# 만약에 변경할 문자가 없는 경우 변경 안됨
# print("replace('a', 'A') :", string0.replace('a', 'A'))
# print(string0)
# string0 = string0.replace('a', 'A') # 이렇게 변수 재지정을 해야 변수에 대한 값이 변경됨
# print(string0)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# bookname = "hello java"
# number = "20B1A"
# print(bookname)
# print(number)
# print()

# print("Q1. bookname에서 'java'를 'python'으로 고치시오.")
# bookname = bookname.replace('java', 'python')
# print(bookname)                          
# print()

# print("Q2.bookname의 문자열 개수를 출력하시오.")
# print(len(bookname))
# print()

# print("Q3.bookname의 문자열를(을) 모두 대문자로 바꾸시오.")
# bookname = bookname.upper()
# print(bookname)
# print()

# print("Q4.두변수의 'A'의 총 개수를 출력하시오.")
# boo = bookname.count('A')
# num = number.count('A')
# print(boo + num)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 문자 포맷팅   => 문자를 표현하는 따옴표안에 포맷팅 기호를 적어야 함 
# 문자 포맷팅을 사용하는 이유 : 여러개의 변수와 문자를 같이 출력하는 경우 콤마(,)를 사용시 의도하지 않은
# 띄어쓰기가 발생하기 때문, 포ㅁ맷팅을 이용하면 내가 원하는 위치에 변수의 값이 들어감

# Hello CIT    <= 이렇게 출력하고 싶음
# a = "Hello"
# b = "CIT"
# print(a,b)                  # 콤마를 사용할 경우 자동으로 띄어쓰기가 되어 출력시 띄어쓰기를 계산을 해야함 
#                             # 그리고 콤마의 경우 사용할 수 있는 수량이 정해져있어 많은 변수의 값을 출력 불가
# print("%s %s" % (a, b))     # 포맷팅을 사용할 경우 내가 원하는 위치에 변수 값이 들어가므로 커스텀이 용이


# 포맷팅 기호   => 따옴표 안에 적어야함
# 문자(str)    => %s
# 실수(float)  => %f
# 정수(int)    =>
# 위 포맷팅 기호는 변수의 자료형의 맞게 사용

# 1. 1개의 변수를 출력할때
# print(" %f " % (변수명))              변수명의 값이 %f 위치에 들어감
# 2. 2개 이상의 변수를 출력할때
# print("%f %s" % (A변수명, B변수명))   A변수명의 값이 %f위치에 들어가고 B변수명의 값이 %s 위치에 들어감


# My name is park! and my age is 15. <=이렇게 출력하고 싶음
# name = "Park"   # 문자이기 때문에 %s
# print("My name is %s! And my age is 15." % (name))

# i = "My"    # 문자이기 때문에 %s
# print("%s name is %s! And my age is 15."% (i, name))

# age = 15    # 정수이기 때문에 %d
# print("%s name is %s! And my age is %d."% (i,name,age))
# print("%d %d" % (age,age))


# 포맷팅의소수점 표시
# 실수의 경우 %f를 사용
# %f 사용시 기본 값은 소수점 6번째 자리 수 까지 출력. 정확히는 7번째자리수에서 반올림한 후 6자리 까지 출력.