# 반복자

# for 문은 시퀀스뿐 아니라 집합과 사전 등 순서가 없는 컬렉션에서도 동작한다. 
# for 문은 반복자(iterator)를 제공하는 데이터라면 모두 순회할 수 있다. 
# 반복자는 다음에 무엇을 출력할 차례인지를 기억하여 데이터를 순서대로 꺼낼 수 있도록 돕는 인터페이스다.

it = iter([1, 2, 3, 4])
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 반복 가능한 데이터: iter() 함수로 반복자를 구할 수 있는 데이터
# 반복자: next() 함수로 값을 하나씩 꺼낼 수 있는 데이터
# iter() 함수: 반복 가능한 데이터를 입력받아 반복자를 반환하는 함수
# next() 함수: 반복자를 입력받아 다음 출력값을 반환하는 함수

# 생성기

# 함수로 생성기를 만들기 위해서는 yield 문이 필요하다. 
# yield 문은 return 문처럼 함수가 값을 반환하고 정지하도록 하는데, 
# 그 함수를 나중에 다시 실행하면 정지했던 위치부터 다시 실행되도록 한다. 
# yield 문이 포함된 함수는 일반 함수와 달리, 호출했을 때 생성기를 반환한다.

def abc():
    """
    a, b, c를 출력하는 생성기를 반환한다.
    """
    yield 'a'
    yield 'b'
    yield 'c'

abc_generator = abc()
print(next(abc_generator))
print(next(abc_generator))
print(next(abc_generator))

def one_two_three():
    """
    1, 2, 3을 출력하는 생성기를 반환한다.
    """
    print('생성기가 1을 반환합니다.')
    yield 1
    print('생성기가 2을 반환합니다.')
    yield 2
    print('생성기가 3을 반환합니다.')
    yield 3

one_two_three_generator = one_two_three()
print(next(one_two_three_generator))
print(next(one_two_three_generator))
print(next(one_two_three_generator))

# 생성기는 반복자의 한 종류다.
# 생성기는 yield 문이 포함된 함수를 실행하여 만들 수 있다.
# yield 문이 포함된 함수를 실행하면 생성기가 반환된다. 생성기를 next() 함수에 전달해 실행시키면 함수의 본문이 실행된다.
# yield 문은 값을 내어준 후 생성기의 실행을 일시정지한다. next() 함수가 실행되면 정지했던 위치에서부터 다시 실행이 이어진다.

# 무한대 범위 자연수 출력 생성자로 흉내

def one_to_infinite():
    """1-무한대의 자연수를 순서대로 내는 생성기를 반환"""
    n = 1
    while True:
        yield n
        n += 1

natural_number = one_to_infinite()
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))
print(next(natural_number))

def countdown(start, end):
    """
    start(포함)부터 end(비포함)까지 거꾸로 세는 생성기를 반환한다.
    """
    n = start       # n은 start에서 시작한다
    while end < n:  # n이 end에 도달하지 않은 동안 반복
        yield n     # 실행이 일시정지되고 n을 반환한다
        n -= 1

print(list(countdown(10,0)))
print(tuple(countdown(10,0)))

# 생성기는 일반적인 반복자처럼 순회할 수 있다.
# 생성기를 이용해 규모가 매우 큰 컬렉션을 흉내낼 수 있다.
# 요소를 생성하는 비용이 큰 컬렉션은 모든 요소를 미리 만들기보다, 
# 생성기를 이용해 그 때 그 때 필요한 요소만 생성하는 편이 좋을 수도 있다.

# 연습문제

import random
print(random.randint(0, 63))
print(random.randint(0, 63))
print([random.randint(0, 63) for e in range(5)])

def random_infinite():
    n = 1       
    while True:  
        yield random.randint(1, n)
        n += 1

random_unit = random_infinite()

print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))
print(next(random_unit))

# 생성기 식

print([e ** 3 for e in range(10)]) # 레인지 범위가 너무 많으면 오래걸리거나 다운

cube_generator = (e ** 3 for e in range(1000000000))
print(next(cube_generator))
print(next(cube_generator))
print(next(cube_generator))
print(next(cube_generator))

# 연습문제

def input_orders(n):
    """n개의 음료를 주문받아 리스트로 반환한다."""
    return (input() for _ in range(n))

# 음료 주문 세 개를 입력받아 각 음료마다 제조 지시한다
for drink in input_orders(3):
    print(drink, '만들어 주세요!')

