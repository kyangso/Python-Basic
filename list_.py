# 변수 = ['값', '값']       => 값의 자료형은 상관없음
# 위형식으로선언
# 리스트란 여러개의자료형을 하나의 변수에순서대로 모아둔것
# 모아둔 자료형의 순서는 0부터 시작한다 => 인덱스(index) 번호라고 얘기
# 리스트의 값을 가지고올때는대괄호([])를이용하여참조

# list1 = [1, 'cit', True]
# print(list1)
# print(list1[0])     # list1 리스트의 0번쨰 값을가지고옴
# print(list1[2])
# print(list1[3])     # list1 리스트의 3번째 값은없으므로에러


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 인덱스 번호를 이용해서 해당번호에 있는 값을 수정할수 있다
# 값 변경은 변수에 값을 저장하는것처럼 진행하면 된다.
# list1 = [1, 'cit', True]
# print(list1)

# list1[1] = 'hello' # list1의 1번째 인덱스의 값을 변경
# print(list1)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# list1 = ['abc', 'dfg', 'hij', 123, 456]
# print(list1)
# print()

# print("Q1. list1의 1번째 원소를 'park'로 고치시오.")
# list1[1] = 'park'
# print(list1)
# print()

# print("Q2. 변수 이름을 'arr'로 하고 아래 리스트를 대입(저장)하시오.")
# arr = [4, 8, 12, 16, 20, 24, 28, 32]
# print(list1)
# print()

# print("Q3. arr의 4번째 원소를 'cit'로 하시오. 단 맨 왼쪽의 원소가 0번째 원소다.")
# arr[4] = 'cit'
# print(arr)
# print()

# print("Q4. print(list1)와 print(arr)을 실행하시오.")
# print(list1)
# print(arr)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# test = ['test', 1, 8, 'hi', '3.15']

# for i in test:  # 기존에 배웠던 for문의 range 자리에 리스트를 넣어서
#                 # 리스트 내용을 전부 출력할수 있음
#     print(i, end=' ')

# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = ['지훈', '서준', '시찬', '윤서']
# score = [92, 96, 98, 100]
# nanugi = int(score[0] + score [1] + score[2] + score[3])

# print('평균은', nanugi / 4, '이고"윤서"가 가장 점수가 높습니다')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 리스트 함수

# 리스트명.insert(인덱스 번호, 추가할 값)
# insert()함수는 인덱스 번호 위치에 값을 추가, 기존 위치에 있는 값은 뒤로 밀림
# 인덱스 번호가 리스트의 범위를 벗어나는 경우 값을 리스트 제일 뒤에 추가됨

# 리스트명.append(추가할 값)
# append()함수는 리스트 제일 뒤에 값을 추가

# del(리스트명[인덱스 번호])
# del()함수는 인덱스 번호에 해당하는 값을 리스트에서 삭제
# 만약 삭제한 위치 뒤에 값이 있으면 앞으로 당겨짐
# 인덱스 번호가 범위를 벗어나면 에러 발생

# 리스트명.remove(삭제할 값)
# remove()함수는 리스트에서 특정 값을 삭제
# 만약 삭제할 값이 여러개면 맨 앞에 있는 한개의 값만 삭제
# 만약 삭제할 값이 리스트에 없으면 에러 발생

# 리스트명.index(인덱스 번호를 찾을 값)
# index()함수는 특정 값의 인덱스 번호를 알려줌
# 특정 값이 여러개일 경우 가장 앞에 있는 인덱스 번호를 알려줌
# 값이 리스트에 없을 경우 에러 발생

# len(리스트명)
# len()함수는 리스트의 크기(길이)를 알려줌

# sum(리스트명)
# sum()함수는 리스트의 값을 전부 더해줌, 리스트 내부의 값이 전부 숫자일때만 가능

# 리스트명.count(개수를 알고 싶은 값)
# count()함수는 특정 값이 리스트에 몇개 있는지 알려줌
# 만약 특정 값이 리스트에 없으면 0

# 리스트명.sort()
# sort()함수는 리스트의 내용을 오름차순으로 정렬

# insert() 와 같이 리스트 변수와 .을 같이 사용하는 함수는 리스트에서만 사용가능하고
# del(), len(), sum()의 경우는 리스트 말고도 다른 자료형에서도 사용가능.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = ['지훈', '서준', '시찬', '윤서']
# score = [92, 96, 98, 100]
# avg =  sum(score) / len(score)

# print('평균은', avg, '이고"윤서"가 가장 점수가 높습니다')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# list0 = []        # 빈 리스트 만들기
# print(list0)
# print()

# print("Q1. append 함수를 사용해 list0에 1,2,3,4,5,6,7,8,9를 차례대로 추가하시오.(반복문을 사용해도 좋다.)")
# for i in range(1, 10, 1) :
#     list0.append(i)
# print(list0)
# print()

# print("Q2. insert 함수를 사용해 list0의 0번째에 0을 추가하시오.")
# list0.insert(0, 0)
# print(list0)
# print()

# print("Q3. del 함수를 이용해 lsit0의 3번째 원소를 삭제 하시오.")
# del(list0[3])
# print(list0)
# print()

# print("Q4. del 함수를 이용해 list0의 5번째 원소를 삭제 하시오.")
# del(list0[5])
# print(list0)
# print()

# print("Q5. remove 함수를 이용해 list0에서 1을 삭제 하시오. ")
# list0.remove(1)
# print(list0)
# print()

# print("Q6. index 함수를 이용해 list0에서 5가 몇번째에 있는지 출력 하시오.")
# print(list0.index(5))
# print()

# print("Q7. index 함수를 이용해 list0에서 6이 존재하는지 확인하시오.몇번째에 위치했는지 출력 하시오")
# try :
#     print(list0.index(6))
# except :
#     print("6이 리스트에 없음")
# print()

# print("Q8. len 함수를 이용해 list0의 원소의 개수를 출력 하시오.")
# print(len(list0))
# print()

# print("Q9. print(list0)을 하여 리스트를 출력 하시오.")
# print(list0)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #



# print("점수를 입력하시오.(끝낼시 0을 입력)")
# listinf = []                    # 반복문안에 리스트관련을 넣을때는 만드는 코드는 무조건 밖에

# while(True):
#     infnum = int(input())       # int(input())코드는 변수랑 같이 써야 저장 가능
#     if(infnum == 0):            # 코드는 순서에 따라 달라짐(위부터 아래)
#         break
#     listinf.append(infnum)      # 어펜드는 맨 뒤에 추가하는것. 쓰는법은 84번 라인 확인
#     # print(listinf)            

# # print(listinf)
# avg = sum(listinf) // len(listinf)
# print("평균은", avg, "입니다.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


