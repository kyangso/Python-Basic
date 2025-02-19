# 딕셔너리(dictionaries)란 키와 값으로 이루어진 것
# 딕셔너리는 인덱스에 대한 개념이 없어 값을 가지고 올때는 키를 이용해서 값을 참조한다.
dicti = {'brand' : 'CIT', 'classnumber' : 4}        # 리스트와 다르게 {}로 되어 있으며, 키와 값은 :로 구분
print(dicti)

dicti['classnumber']
print(dicti['classnumber'])         # 딕셔너리는 값을 참조할떄 키를 이용하여 참조한다.

dicti['classnumber'] = 10           # 값을 바꿀때도 키를 이용해서 바꾼다. 
print(dicti['classnumber'])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
