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


string0 = 'cit academy'
print (string0)
print()

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


bookname = "hello java"
number = "20B1A"
print(bookname)
print(number)
print()

print("Q1. bookname에서 'java'를 'python'으로 고치시오.")
bookname = bookname.replace('java', 'python')
print(bookname)                          
print()

print("Q2.bookname의 문자열 개수를 출력하시오.")
print(len(bookname))
print()

print("Q3.bookname의 문자열를(을) 모두 대문자로 바꾸시오.")
bookname = bookname.upper()
print(bookname)
print()

print("Q4.두변수의 'A'의 총 개수를 출력하시오.")
boo = bookname.count('A')
num = number.count('A')
print(boo + num)


