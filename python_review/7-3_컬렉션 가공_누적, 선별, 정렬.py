# 컬렉션 가공

prices = [2500, 3000, 1800, 3500, 2000, 3000, 2500, 2000]

# for 문으로 모든 요소에 연산 적용하기

new_prices = []
for price in prices:
    new_prices.append(price+50)

# 더 간단하게 리스트 조건 제시법

# 원소나열법: [2, 4, 6, 8, 10]
# 레인지: 2 이상 11 미만의 2씩 증가하는 수의 리스트
# 조건제시법: [1, 2, 3, 4, 5]의 각 요소에 2를 곱한 리스트

# 원소나열법은 모든 요소를 직접 기술하는 방법이고, 레인지는 범위와 간격으로 등차수열을 나타내는 방법이다. 
# 리스트 조건제시법은 컬렉션의 각 요소에 지정된 조건(연산)을 적용해 새 리스트를 만드는 방법이다. 
# 원소나열법과 레인지는 새 리스트를 바로 정의할 수 있지만, 조건제시법은 기존에 정의된 컬렉션이 있어야 한다.

new_prices2 = [e * 50 for e in prices]

# map() 함수

# 여기서 리스트 조건제시법과 유사한 기능을 하는 함수, map()을 봐 두면 좋다. 
# 리스트 조건제시법은 파이썬 문법에 정의된 ‘식’이고 map()은 일반적인 ‘함수’다. 
# map() 함수는 각 요소에 적용할 연산(함수)과 컬렉션을 전달받아, 컬렉션의 모든 요소에 연산을 적용한다.

new_prices3 = list(map(lambda n : n + 50, prices))

# 연습문제

multuply = [e * e for e in range(0, 10)]
multuply2 = list(map(lambda n : n * n, range(0, 10)))

print(multuply, multuply2)

# 모든 요소 누적하기

total_price = 0           # ❶ 총 가격을 저장할 변수
num_items = 0             #  전체 항목 개수를 저장할 변수

for price in prices:      # ❷ prices의 모든 요소를 순회하며
    total_price += price  # 각 음료 가격을 누적하고 (총 가격 구하기)
    num_items += 1        # 전체 항목 개수를 1씩 증가시킨다 (전체 항목 개수 세기)

most_expensive = 0              # ❶ 가장 비싼 가격을 기억할 변수

for price in prices:            # ❷ prices의 모든 요소를 순회하며
    if most_expensive < price:  # ❸ 요소가 가장 비싼 가격보다 크면
        most_expensive = price      # 이 요소를 가장 비싼 가격으로 기억한다

# 연습문제
def length(seq):
    items = 0
    for i in seq:
        items += 1
    return items

seq = {'하나', 2, 5, 6, '둘'}
print(length(seq))

def longest(*args):
    j = args[0]
    for i in args:
        if length(j) < length(i):
            j = i
    return j

print(longest([1, 2, 3], (4, 5), [], 'abcdefg', range(5)))
print(longest('파이썬', '프로그래밍'))
print(longest(range(10), range(100), range(50)))

# 선별하기

filtered_prices = []                   # ❶ 조건에 맞는 가격을 담을 리스트

for price in prices:                   # ❷ prices 리스트의 모든 요소를 순회하며
    if price <= 2000:                  # ❸ 각 요소가 조건에 맞는 경우
        filtered_prices.append(price)  # 새 리스트에 담는다

filtered_prices = [price for price in prices if price <= 2000]

filtered_prices = list(filter(lambda n : n <= 2000, prices))

# 연습 문제

용의자들 = [
    {'이름': '멍멍', '털': '흰색', '주둥이': '크다', '발': '크다'},
    {'이름': '킁킁', '털': '검은색', '주둥이': '작다', '발': '크다'},
    {'이름': '왈왈', '털': '흰색', '주둥이': '작다', '발': '크다'},
    {'이름': '꿀꿀', '털': '검은색', '주둥이': '작다', '발': '작다'},
    {'이름': '낑낑', '털': '흰색', '주둥이': '작다', '발': '작다'},
]

filtered_용의자 = []

for 용의자 in 용의자들:
    if 용의자['털'] == '흰색':
        if 용의자['주둥이'] == '작다':
            if 용의자['발'] == '크다':
                filtered_용의자.append(용의자)

print(용의자['이름'])

diameters = [0.985, 0.992, 1.004, 0.995, 0.899, 1.001, 1.002, 1.003, 1.009, 0.998]

def faulty_rate(dia):
    fault = 0
    success = 0
    for k in dia:
        if k >= 0.99 and k < 1.01:
            success += 1
        else:
            fault += 1
    return fault/len(dia)

print(faulty_rate(diameters))

# 정렬하기

# 거품 정렬(bubble sort): 바로 옆의 두 요소를 각각 비교하는 알고리즘. 비효율적이고 정렬 속도가 느리지만 단순해서 쉽게 이해할 수 있다.
# 퀵 정렬(quicksort): 요소 하나를 기준점으로 삼고 그보다 작은 요소와 큰 요소를 나누어 배치하는 과정을 반복하는 알고리즘.
# 삽입 정렬(insertion sort): 각 요소를 이미 정렬된 부분의 제 위치에 삽입하는 과정을 반복하는 알고리즘.
# 합병 정렬(merge sort): 전체를 작은 단위로 나눈 후 다시 합치면서 정렬하는 알고리즘.

coll = [10, 5, 1, 9, 7, 3]

for _ in coll:                      # ❶ 컬렉션의 요소의 개수만큼 반복하여
    for i in range(len(coll) - 1):  # ❷ 각 주기마다 거품 정렬의 한 단계를 수행한다
        if coll[i] > coll[i + 1]:
            coll[i], coll[i + 1] = coll[i + 1], coll[i]

print(coll)  # [1, 3, 5, 7, 9, 10]

# sorted() 함수

print(sorted([10, 5, 1, 9, 7, 3]))
print(sorted([10, 5, 1, 9, 7, 3], reverse=True))

# 절대값으로 비교하기
print(sorted([3, -5, 1, -2, -4], key=abs))

# 사전의 특정 키-값으로 비교

items = [
     {'name': '아메리카노', 'price': 2000},
     {'name': '카페 라테', 'price': 2500},
     {'name': '카푸치노', 'price': 2400},
]

sorted_items = sorted(items, key=lambda item: item['price'])
import pprint
pprint.pprint(sorted_items)

# 연습문제

fruits = ['배', '사과', '복숭아', '블루베리']
print(sorted(fruits, key=len, reverse=True))

