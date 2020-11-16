# 컬렉션 순회하기

for element in ['a', 'b', 'c', 'd']:
    print(element)

for element in ('월', '화', '수'):  # 튜플 순회하기
    print(element)

for character in '가나다라':        # 문자열 순회하기
    print(character)

for n in range(10):                 # 레인지 순회하기
    print(n)

# 집합과 매핑 순회하기

for element in {'사자', '박쥐', '늑대', '곰'}:
    print(element)

drinks = {
    '아메리카노': 2500,
    '카페 라테': 3000,
    '딸기 주스': 3500,
}

for k in drinks:
    print(k)          # ❶ 변수에는 사전의 키들이 대입된다
    print(drinks[k])  # ❷ 키를 이용해 값을 구할 수도 있다.

for k, v in drinks.items(): # 키와 값을 쌍을 요소로 갖는 시퀀스 반환
    print(k)
    print(v)

happiness = {
    '호주': 7.95,
    '노르웨이': 7.9,
    '미국': 7.85,
    '일본': 6.2,
    '한국': 5.75,
}

for k, v in happiness.items():
    print('{} 사람들은 {} 만큼 행복합니다'.format(k, v))

board = [
    [['black', '룩'], None, None, None, None, None, None, None],
    [None, None, None, ['black', '킹'], None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, ['white', '비숍'], None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, ['white', '킹'], None, None, None],
]

for row in board:  # 체스판(바깥쪽 리스트)의 각 행(요소)을 순회한다
    print(row)     # 각 행을 화면에 출력한다

for row in board:                 # ❶ 체스판(바깥쪽 리스트)의 각 행(요소)을 순회한다
    for piece in row:             # ❷ 행(안쪽 리스트)의 각 체스말(요소)을 순회한다
        if piece:                 # ❸ 체스말이 있으면 I를, 없으면 .을 출력한다
            print('I', end=' ')
        else:
            print('.', end=' ')
    print()                       # ❹ 바깥쪽 리스트를 순회할 때마다 행을 바꾼다

# 연습 문제

천간 = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
지지 = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

for i in 천간:
    for j in 지지:      
            print(i+j, end=' ')
    print()

# 여러 개의 컬렉션을 나란히 순회하기

seasons = ['봄', '여름', '가을', '겨울']
mountains = ['금강산', '봉래산', '풍악산', '개골산']

for i in range(4):    
    print('{}에는 {}'.format(seasons[i], mountains[i]), end=' ')
    print()

for season, mountain in zip(seasons, mountains):    
    print('{}에는 {}'.format(season, mountain), end=' ')
    print()

# 연습문제

def plus_elements(numbers1, numbers2):
    plus_list = []
    for i, j in zip(numbers1, numbers2):
        plus_list.append(i+j)
    return plus_list

print(plus_elements((1,2,3), [4,5,6]))