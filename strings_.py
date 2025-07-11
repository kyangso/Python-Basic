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

# split(문자열)
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
# P = "CIT" 
# I = "the"   
# E = "best"
# Y = "academy"
# M = '!'
# F = "음식이"
# G = "친절하고"
# J = "선생님이"
# N = "맛있어용^^"  # 문자이기 때문에 %s
# print("%s %s %s %s%s %s %s %s %s" % (I,E,Y,P, M, F,G,J,N))

# i = My    # 문자이기 때문에 %s
# print("%s name is %s! And my age is 15."% (i, name))

# age = 15    # 정수이기 때문에 %d
# print("%s name is %s! And my age is %d."% (i,name,age))
# print("%d %d" % (age,age))


# 포맷팅의소수점 표시
# 실수의 경우 %f를 사용
# %f 사용시 기본 값은 소수점 6번째 자리 수 까지 출력. 정확히는 7번째자리수에서 반올림한 후 6자리 까지 출력.
# pi = 3.1415
# print("%f" % (pi))  # 만약 변수 값이 6자리 보다 작으면 나머지 소수점 자리의 숫자는 0으로 출력

# %.숫자f       => 소수점 숫자 번째 까지 출력. 정확히는 숫자 + 1 자리수에서 반올림한 후 숫자 번째 자리수까지 출력
# print("%.3f" % (pi))    # 소수점 4번째 자리에서 반올림한 후 소수점 3째 자리까지지


# 포맷팅을 이용해서 문자열을 정렬 할수 있다.
# 100000
#  10000
#   1000
# 위와 같이 출력하고 싶을경우
# a = 100000
# b = 10000
# c = 1000
# print("%7d" % a)
# print("%7d" % b)
# print("%7d" % c)

# 포맷팅 기호 사이에 숫자를 넣을수 있음
# %7d   =>   7칸의 공간에서 출력할 값을 오른쪽에 붙여 출력
# %-7d  =>   7칸의 공간에서 출력할 값을 외앤쪽에 붙여 출력
# 만약 출력할 내용이 7칸보다 클경우 왼쪽에 붙여 출력
# c = 888822222
# print("%7d" % c)
# print("%-7dhi" % c)

# 위와 같이 정렬에 대한 것은 %s, %d, %f 전부 가능

# pi = 3.14159265
# print("%-6.3fhi" % pi)      # 3.142가 출력된 이유는 4번째 자리에 값이 5이므로 반올림, . 로 한자리로 포함함


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 이스케이프 코드
# 특별한 문자로 문자 출력시에 사용한다  => 따옴표 기호(' '," ")안에 있음
# \n    문자열 안에서 줄을 바꿀때 사용
# \t    문자열 사이에 탭 간격을 줄때 사용
# \\    문자열 /를 그대로 표현할때 사용
# \'    ' 을 출력
# \"    " 을 출력

# print("야!!!!!!\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n구르트 아줌마\t 3000원")     # \n 사용
# print("금 덩 이\t12억3000만원")     # \t 사용
# print("Hello\\CIT")     # \\ 사용
# print("\' \"")



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# name = ["bell", "sona", "rick", "tony", "jade"]
# score = [ 52, 96, 32, 73, 85]
# print(name)
# print(score)
# print()

# print("Q1.name에서 \"sona\"를 \"kona\"로 바꾸시오.replace 함수 이용")
# if('sona' in name) :                                # 리스트에 sona가 있는지 확인
#     idx = name.index("sona")                        # 값 변경을 위한 'sona'의 인덱스 번호 찾아 idx 변수에 저장
#     name[idx] = name[idx].replace("sona", "kona")   # replace()함수를 이용하여 'sona'를 'kona'로 변경경
# else:                                               # 'sona'가 리스트에 없는 경우우
#     print("sona 없음")
# print(name)
# print()


# print("Q2.name의 모든 'o'를 \"ecoto\"로 바꾸시오.")
# for idx in range(0, 5, 1) :                              # 여러번 반복할떈 반복문 사용
#                                                          # 문자열에서 대체할땐 무조건 replace(그전에 먼저 idx번호를 알아내고)
#     if('o' in name[idx]) :
#         name[idx] = name[idx].replace('o', 'ecoto')
# print(name)
# print()

# print("Q3.name의 원소들을 모두 출력을 하시오.")
# print(name)
# print()

# print("Q4.name 리스트에서 'co'가 있으면 분할하여 name 리스트의 맨 뒤에 추가하시오")                                                                                         
# for i in name:                       # name 리스트의 값을 전체 반복 하여 변수1에저장                                                                                               
#     if("co" in i):                   # i에'co'가 있을경우 실행,즉 문자열 안에   'co'가 있으면 실행                                  
#         idx = name.index(i)          # 값 삭제및 변경을 위해 'co'가 들어간 문자열의 인덱스 번호를 찾아 idx변수에 저장
#         sp = i.split("co")           # 'co'가 들어간 문자열을 'co'기준으로 나눔
#                                      # split()를 사용하면 나눠진 문자열은 리스트 형태로 sp변수에 저장
#         del(name[idx])               # 'co'가 들어간 문자열은 리스트에서 삭제
#         # name = name + sp           # 'co'를 기준으로 나눠진 리스트(sp)와 기존의 리스트(name)를 더함
#                                      # append를 안하는 이유는 append를 사용할 경우 2중 리스트가 됨
#                                      # 아래 반복문을 사용하던지, 현재 코드의 리스트의 덧셈을 사용하던지 둘중 하나를 진행해야함

#                                      # 반복문을 사용하여 분할된 문자열이 있는 sp리스트의 값을 name변수에 저장
#         for k in sp:
#             name.append(k)
# print(name)
# print()

# print("Q5.name의 원소들을 모두 출력을 하시오.")
# print(name)
# print()

# print("Q6.score의 평균을 구하고 출력을 하시오.")
# avg = sum(score) / len(score)
# print(avg)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 문자열 합치기
# + 기호를 이용하면 문자열을 합칠수 있음
# a = "바"
# b = "보"
# c = a + b
# print(c)

# 문자와 숫자의 연산
# 문자와 숫자의 경우 곱하기 (*)만 ㄱㄴ
# print("헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤헤" * 10)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Q1. \"abc\"를 값으로 가지는 문자열 변수 A1를 만드시오")
# A1 = "abc"
# print("A1 =", A1)
# print()

# print("Q2. \"ABC\"를 값으로 가지는 문자열 변수 A2를 만드시오")
# A2 = "ABC"
# print("A2 =", A2)
# print()

# print("Q3. A1과 A2를 합쳐 \"abcABC\"를 값으로 가지는 문자열 변수 B1를 만드시오")
# B1 = A1 + A2
# print("B1 =", B1)
# print()

# print("Q4.B1에서 2번째부터 4번째 문자 \"cAB\"와\"LE\"를 합쳐만든 변수 C1를 만드시오")           # 문자에서 어떤 파트만 가져올땐 slice 사용(문자열 한정)
# C1 = B1[2:5] + "LE"                                                                         # + 활용해서 두개의 문자열 (or 변수) 합체
# print("C1 =", C1)
# print()

# print("Q5. C1의 첫글자를 대문자로 고치시오")
# C1 = C1.upper()                                                             # 모든걸 다 대문자로 할떈 upper 사용
# print("C1 =", C1)
# print()

# print("Q6. C1과 \"CAR\"을 합쳐서 출력하시오")
# C2 = C1 + "CAR"                                                         # 합체할떈 + 사용
# print(C2)


