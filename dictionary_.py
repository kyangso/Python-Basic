# 딕셔너리(dictionaries)란 키와 값으로 이루어진 것
# # 딕셔너리는 인덱스에 대한 개념이 없어 값을 가지고 올때는 키를 이용해서 값을 참조한다.
# dicti = {'brand' : 'CIT', 'classnumber' : 4}        # 리스트와 다르게 {}로 되어 있으며, 키와 값은 :로 구분
# print(dicti)

# dicti['classnumber']
# print(dicti['classnumber'])         # 딕셔너리는 값을 참조할떄 키를 이용하여 참조한다.

# dicti['classnumber'] = 10           # 값을 바꿀때도 키를 이용해서 바꾼다. 
# print(dicti['classnumber'])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 딕셔너리의 값 삼입과삭재

# test = {'a' : 213}
# print(test)
# print()

# 삽입
# 딕셔너리명ㅇ[키] = 값

# test['class'] = 1 
# print(test)
# print()

# 삭제
# 딕셔너리명.pop(키)
# # pop 함수를 사용하여 키와 값을 둘다 삭제한다.
# test.pop('class')
# print(test)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("1 브랜드를 키로, 가격을 값으로 하여 딕셔너리를 만드시오 단, 변수이름은 'Americano'로 하시오")
# Americano = {'Starlucks' : 3700, 'Mollys' : 4100, 'Emiya' : 2800, 'FomAFams' : 4100}
# print(Americano)
# print()

# print("2 위에서 만든 딕셔너리에서 다음 데이터를 추가하시오")
# Americano['Anzelinus'] = 4900
# Americano['Coffejeans'] = 4800
# print(Americano)
# print()

# print("3 위에서 만든 딕셔너리에서 Emiya와 FomAFams 브랜드를 삭제하시오.")
# Americano.pop('Emiya')
# Americano.pop('FomAFams')
# print(Americano)
# print()

# print("4 print(Americano)를 통해 아래처럼 출력되는지 확인 하시오")
# print(Americano)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks' : 3700, 'Mollys' : 4100, 'Anzelinus' : 4900, 'Coffeejean' : 4800}
# print(Americano)
# print()


# 딕셔너리 for문의 특징
# 키만 출력
# for i in Americano:
#     print(i)
# print()

# 값만 출력
# for i in Americano.values():    # values() 함수를 사용
#     print(i)
# print()

# for x in Americano :
#     print(Americano[x])         # 키를 이용
# print()

# 키와 값 모두 출력
# for x, y in Americano.items() : # items()함수 사용, for문 변수 2 개를 사용해야함
#     print(x,y)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks' : 3700, 'Mollys' : 4100, 'Anzelinus' : 4900, 'Coffeeejean' : 4800}
# print('#1 모든 브랜드를 출력하시오')
# for i in Americano :
#     print(i, end=" ")
# print()
# print()

# print('#2 아메리카노 가격의 합을 구하시오.')
# hapge = 0                       # 누적 덧셈 등 반복문에 변수가 필요한 경우 변수는 무조건 반복문 밖에
#                                 # 어떤 기능(을/를)만들거나 추가할땐 변수를 최소 1개 이상 만드는게 쉽다.
# for i in Americano.values():
#     hapge = hapge + i           # hapge += i

# print(hapge)
# print()

# print("#3 아메리카노 가격읭 평균을 구하시오.")
# print(hapge // len(Americano))  # //쓰면 소수단위가 안된다.
# print()

# print("#4 itmes()함수를 이용하여 오른족관 같이 추가하시오")
# for key, value in Americano.items():
#     print('brand:', key, ", price:", value)