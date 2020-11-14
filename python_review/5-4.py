# 집합

# 순서나 키 없이, 포함되는 원소를 모아 둔 데이터 구조다.
# 원소를 중복으로 저장하지 않는다.
# 합집합, 교집합 같은 수학의 집합 연산이 가능하다.
# 어떤 원소가 집합에 포함되었는지 검사할 수 있다.

# three = list(range(0, 1000, 3))[1:]
# four = list(range(0, 1000, 4))[1:]
# sum_th_f = set(three + four)
# print(len(sum_th_f))

# 합집합

들짐승 = {'사자', '박쥐', '늑대', '곰'}
날짐승 = {'독수리', '매', '박쥐'}
바다생물 = {'참치', '상어', '문어 괴물'}

짐승 = 들짐승.union(날짐승)
짐승2 = 들짐승 | 날짐승
짐승3 = 들짐승 | 날짐승 | {'인간'}

# 교집합

두짐승 = 들짐승.intersection(날짐승)
두짐승2 = 들짐승 & 날짐승

# 차집합

차짐승 = 짐승.difference(날짐승)
차짐승2 = 날짐승 - 들짐승

# 대칭차

대칭짐승 = 들짐승.symmetric_difference(날짐승)
대칭짐승 = 들짐승 ^ 날짐승

# 부분집합 확인

print(들짐승.issubset(짐승))
print(들짐승 <= 짐승)
print(들짐승.issubset(날짐승))
print(들짐승 <= 날짐승)

# 서로소 확인
print(들짐승.isdisjoint(날짐승))

# 원소 변경

# add(데이터): 데이터를 원소로 추가
# discard(원소): 원소 제거
# remove(원소): 원소 제거 (원소가 없으면 오류)
# pop(): 아무 원소나 꺼낸다 (집합이 비어있으면 오류)
# clear(): 모든 원소를 제거

들짐승.add('인간')
print(들짐승)
들짐승.discard('인간')
print(들짐승)
들짐승.remove('박쥐')
print(들짐승)
들짐승.pop()
print(들짐승)
들짐승.clear()
print(들짐승)

all_days = {'월', '화', '수', '목', '금', '토', '일'}
work_days = {'월', '화', '수', '목', '금'}
wekends = {'토', '일'}

def is_working_day(day) : 
    if day <= work_days :
        return True
    else :
        return False

print('오늘은 무슨 요일입니까?')
day = set(input())

if is_working_day(day) :
    print('출근을 축하합니다.')
else :
    print('휴일을 축하합니다.')

# 프로즌셋

# 수정이 불가능한 집합 컬렉션

# 공집합 프로즌셋: frozenset()
# 집합에서 정의하기: frozenset({원소 1, 원소 2, 원소 3, ...})
# 시퀀스에서 정의하기: frozenset([원소 1, 원소 2, 원소 3, ...])