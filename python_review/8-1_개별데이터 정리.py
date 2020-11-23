# 개별 데이터 정리

coordinate_1 = {'x': 5, 'y': 3}   # ❶ 점 (좌표)

triangle_1 = {                    # ❷ 삼각형
    'point_a': {'x': 0, 'y': 0},  #    삼각형의 각 꼭지점을
    'point_b': {'x': 3, 'y': 0},  #    좌표로 나타냈다
    'point_c': {'x': 3, 'y': 4},
}

rectangle_1 = {                   # ❸ 사각형
    'point_a': {'x': 2, 'y': 2},  #    꼭지점이 네 개라서
    'point_b': {'x': 6, 'y': 2},  #    좌표도 네 개다
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}

import math

def square(x):
    return x*x

def distance(point_a, point_b):
    return math.sqrt(square(point_a['x'] - point_b['x']) + square(point_a['y'] - point_b['y']))

def circumference_of_triangle(shape):
    """삼각형 데이터를 전달받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_a = distance(shape['point_c'], shape['point_a'])
    return a_to_b + b_to_c + c_to_a

def circumference_of_rectangle(shape):
    """사각형 데이터를 전달받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_d = distance(shape['point_c'], shape['point_d'])
    d_to_a = distance(shape['point_d'], shape['point_a'])
    return a_to_b + b_to_c + c_to_d + d_to_a

print(circumference_of_triangle(triangle_1))
print(circumference_of_rectangle(rectangle_1))


# 개별 데이터를 정의하기 위한 유형을 약속하기

coordinate_2 = (3, 5)                  # ❶ 점 (좌표)

triangle_2 = ((0, 0), (0, 3), (4, 3))  # ❷ 삼각형

rectangle_2 = {                        # ❸ 사각형
    'point': (2, 2),
    'width': 4,
    'height': 4,
}

# 유형: '좌표'는 다음 키를 갖는 사전이다.
#     * 'x': x 축의 위치 (정수)
#     * 'y': y 축의 위치 (정수)
coordinate_1 = {'x': 5, 'y': 3}

# 유형: '삼각형'은 다음 키를 갖는 사전이다.
#     * 'point_a': 첫번째 점의 위치 (좌표)
#     * 'point_b': 두번째 점의 위치 (좌표)
#     * 'point_c': 세번째 점의 위치 (좌표)
triangle_1 = {
    'point_a': {'x': 0, 'y': 0},
    'point_b': {'x': 3, 'y': 0},
    'point_c': {'x': 3, 'y': 4},
}

# 유형: '사각형'은 다음 키를 갖는 사전이다.
#     * 'point_a': 첫번째 점의 위치 (좌표)
#     * 'point_b': 두번째 점의 위치 (좌표)
#     * 'point_c': 세번째 점의 위치 (좌표)
#     * 'point_d': 네번째 점의 위치 (좌표)
rectangle_1 = {
    'point_a': {'x': 2, 'y': 2},
    'point_b': {'x': 6, 'y': 2},
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}

# 연습문제

# 유형: '체스말'은 다음 키를 갖는 사전이다.
#       * 'x' : x 축의 위치(알파벳)
#       * 'y' : y 축의 위치(정수)
#       * 'color' : 체스말의 색('black', 'white')
#       * 'role' : 체스말의 역할('룩', '킹', '퀸', '비숍', '나이트', '폰')
체스말1 = {'type': '체스말', 'x': 'A', 'y': '8', 'color': 'black', 'role': '룩'}
체스말2 = {'type': '체스말', 'x': 'E', 'y': '1', 'color': 'white', 'role': '킹'}

# 유형: '바둑돌'은 다음 키를 갖는 사전이다.
#       * 'x' : x 축의 위치(정수)
#       * 'y' : y 축의 위치(정수)
#       * 'order' : 몇 수쨰에 둔 것인지(정수)
#       * 'color' : 바둑돌의 색('흑', '백')
바둑돌1 = {'type': '바둑돌', 'x': 8, 'y': 14, 'order': 83, 'color': '흑'}
바둑돌2 = {'type': '바둑돌', 'x': 12, 'y': 3, 'order': 84, 'color': '백'}


# 데이터의 유형 구별하기

triangle_3 = {
    'type': '삼각형',             # 데이터의 유형을 나타내는 정보
    'point_a': {'x': 0, 'y': 0},
    'point_b': {'x': 3, 'y': 0},
    'point_c': {'x': 3, 'y': 4},
}

rectangle_3 = {
    'type': '사각형',             # 데이터의 유형을 나타내는 정보
    'point_a': {'x': 2, 'y': 2},
    'point_b': {'x': 6, 'y': 2},
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}

def circumference(shape):
    """도형 데이터를 전달받아 둘레를 구해 반환한다."""
    
    if shape['type'] == '삼각형':    # type() 함수 대신 인덱싱 연산 사용
        a_to_b = distance(shape['point_a'], shape['point_b'])
        b_to_c = distance(shape['point_b'], shape['point_c'])
        c_to_a = distance(shape['point_c'], shape['point_a'])
        return a_to_b + b_to_c + c_to_a
    
    elif shape['type'] == '사각형':  # type() 함수 대신 인덱싱 연산 사용
        a_to_b = distance(shape['point_a'], shape['point_b'])
        b_to_c = distance(shape['point_b'], shape['point_c'])
        c_to_d = distance(shape['point_c'], shape['point_d'])
        d_to_a = distance(shape['point_d'], shape['point_a'])
        return a_to_b + b_to_c + c_to_d + d_to_a
    
    else:
        return None


# 연습문제
def print_piece(point):
    """체스말, 바둑돌 데이터를 전달받아 안내한다."""
    if point['type'] == '체스말':    # type() 함수 대신 인덱싱 연산 사용
        print('{} {}이 {}{} 위치에 놓여 있어요'.format(point['color'], point['role'], point['x'], point['y']))
    elif point['type'] == '바둑돌':  # type() 함수 대신 인덱싱 연산 사용
        print('제 {} 수: {}이 ({}, {}) 위치에 두었습니다.'.format(point['order'], point['color'], point['x'], point['y']))
    else:
        return None

print_piece(체스말1)
print_piece(바둑돌2)