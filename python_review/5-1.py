# 챕터 5 데이터 관리

# 시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열
# list, tuple, range, string 등 여러 시퀀스 컬렉션 제공

# 리스트

# 리스트 표현

number_list = [1, 2, 3, 4, 5]
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

3 in number_list # 리스트안에 3이 있는 지 확인
'z' not in alphabet_list # 리스트안에 z가 없는 지 확인

len(number_list) # 리스트 길이 확인
sum_list = number_list + alphabet_list # 리스트 두 개 합쳐서 저장
mul_list = number_list * 2 # 리스트 반복 후 저장

# 슬라이싱
print(alphabet_list[2:6]) # 2 이상 6 미만 위치의 범위 출력
print(alphabet_list[:3]) # 3 미만 위치의 범위 출력
print(alphabet_list[5:]) # 5 이상 위치의 범위 출력
print(alphabet_list[:]) # 전체 범위 출력

# 간격 지정 슬라이싱
print(alphabet_list[::2]) # 전체 범위에서 두 요소마다 하나씩 선택
print(alphabet_list[1::2]) # 1 이상의 범위에서 두 요소마다 하나씩 선택
print(alphabet_list[::-1]) # 전체 범위에서 뒤에서부터 한 요소마다 하나씩 선택

# 리스트 복사
original_list = ['a', 'b', 'c']
assigned_list = original_list # 동일 시퀀스 할당
copied_list = original_list[:] # 시퀀스 복사

# 통계 함수
print(sum(number_list))
print(min(number_list))
print(max(number_list))

def mirror(sequence):
    sequence2 = sequence[3::-1]
    print(sequence + sequence2)

mirror(number_list)

# 시퀀스 조작 메서드
# numbers = [6, 7, 8, 9, 10]
# number_list.append(numbers)
# number_list.insert(1, numbers)
# number_list.extend(numbers)
# number_list += [1,2,3]
# number_list.pop()
# number_list.remove(1)
# print(number_list)
# number_list.clear()
# print(number_list)