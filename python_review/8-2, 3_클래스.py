# 클래스와 객체

# 클래스: 데이터 유형

# 데이터: 값과 유형으로 구성된 정보.
# 데이터 유형: 데이터가 어떤 범주에 속하는지를 나타내는 데이터의 구성요소. 클래스로 표현된다.
# 클래스: 데이터 유형을 나타내는 데이터. int, float, str 등이 있다.

# 객체: 개별 데이터

# 객체에는 값(value)·유형(type)·정체성(identity)이라는 세 특성이 있다. 
# 값은 메모리에 기록된 내용이다. 가변 객체는 값이 바뀔 수 있지만 불변 객체는 값이 바뀌지 않는다. 
# 유형은 데이터의 종류로, 유형에 따라 그 값을 어떻게 읽고 다루어야 할지가 결정된다. 
# 정체성은 각각의 객체를 식별하기 위한 고유번호로, 객체가 메모리 속에서 위치한 주소 값이기도 하다. 
# 값과 유형이 동일한 데이터가 데이터가 메모리 공간에 여러 개 존재할 수 있지만, 이들은 서로 별개의 객체이며 정체성이 서로 다르다.

# 클래스와 인스턴스의 관계

# 객체가 어떤 클래스에 속할 때, 그 객체를 그 클래스의 인스턴스(instance)라고 부른다. 
# 영어 단어 ‘instance’는 ‘사례’라는 뜻이다. 
# 어떤 범주에 속하는 사례는 여러 가지가 될 수 있듯이, 클래스에 속하는 인스턴스도 여러 개 존재할 수 있다. 
# 1, 2, 3, 4는 모두 int 클래스의 인스턴스다.

# 클래스 정의하기

# class 문

# class 클래스이름:    # ❶ 첫 행
#     """독스트링"""   # ❷ 클래스의 의미와 역할 설명
#     본문             # ❸ 클래스 공용 속성 정의

# 파스칼 표기법(PascalCase): PythonProgramming처럼 단어와 단어를 대문자로 구별하는 방법이다. 파이썬 프로그래밍에서 클래스 이름을 지을 때 사용한다.
# 뱀 표기법(snake_case): python_programming처럼 단어와 단어를 밑줄 기호로 구별하는 방법이다. 파이썬 프로그래밍에서 변수·함수의 이름을 지을 때 사용한다.
# 낙타 표기법(camelCase): pythonProgamming처럼 대문자로 단어를 구별하되 첫 단어는 소문자로 쓰는 방법이다. 파이썬 프로그래밍에서는 잘 사용되지 않는다.

class Cake:
    """케이크를 나타내는 클래스"""
    coat = '생크림'

print(Cake)
cake_1 = Cake()
cake_2 = Cake()
print(type(cake_1))
print(isinstance(cake_2, Cake))

# 속성과 이름공간

# 클래스 속성
# 클래스.속성과 같이 클래스 이름 뒤에 점 기호(.)를 붙여 표현한다.
# 일반적으로 클래스의 속성은 class 문에서 확정하고, 나중에는 수정하지 않는다. 
# 클래스의 속성은 모든 인스턴스가 공유하는 데이터여서 마구 바꾸면 혼란스럽다.

# 인스턴스 전용 속성
#  인스턴스에 속성을 추가하려면 인스턴스.속성 = 값과 같이 인스턴스 속성 이름을 쓰고 값을 대입하면 된다.

# 클래스 속성: 클래스의 전체 특성을 나타내는 정보. 클래스 속에 정의된 이름이며 클래스에 속하는 인스턴스가 공유한다.
# 인스턴스 속성: 인스턴스의 고유한 특성을 나타내는 정보. 인스턴스 속에 정의된 이름이며 인스턴스마다 각자 따로 갖는다.

# 이름공간

# 이름공간은 프로그래밍 언어에서 이름이 가리키는 대상을 제한하는 범위다. 
# 클래스와 인스턴스는 이름공간이기 때문에, 그 안에서 짧고 간편한 이름을 사용할 수 있다. 
# 같은 이름이 여럿 있더라도 문맥에 따라 무엇을 가리키는지 알 수 있다.

# dir() 함수로 이름공간에 정의된 이름 구하기
import pprint
pprint.pprint(dir(Cake))

# 연습문제

class Coordinate:
    """좌표를 나타내는 클래스"""
    x = 0
    y = 0

point_1 = Coordinate()
point_2 = Coordinate()

point_1.x = -1
point_1.y = 2
point_2.x = 2
point_2.y = 3

import math

def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

def distance(point_a, point_b):
    """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
    return math.sqrt(square(point_a.x - point_b.x) + square(point_a.y - point_b.y))

print(distance(point_1, point_2))

# 메서드

# 클래스나 인스턴스에 속한 함수는 그 데이터 종류를 위한 전용 함수로 기능하게 된다. 이 함수를 메서드(method)라고 부른다.
# class 클래스이름:
#     """독스트링"""
#     클래스 공용 속성
    
#     def 메서드():
#         """이 클래스를 다루는 함수"""
#         메서드 본문
    
#     ...(필요한 만큼 메서드를 추가 정의)

class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'
    #                                                           ❶ 빈 행
    def describe(self):                                           # ❷ 메서드 정의하기
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.coat, '으로 덮여 있다.')      # ❸

cake_1 = Cake()  # 클래스를 새로 정의했으니, 인스턴스도 새로 생성해야 한다
cake_1.coat = '초콜릿'
cake_1.describe()

# 메서드는 클래스와 인스턴스의 속성으로 정의된 함수이며, 특정 데이터 유형을 다루는 방법을 나타낸다.
# 메서드는 대부분 class 문 내부에서 클래스 공용 속성으로 정의된다.
# 메서드는 클래스 또는 인스턴스를 기준으로 호출할 수 있다. 
# 인스턴스를 기준으로 호출할 때는 인스턴스가 메서드에 전달된다. 
# 이를 통해 메서드에서 인스턴스 전용 속성에 접근할 수 있다.

# 연습 문제
class Coordinate:
    """좌표를 나타내는 클래스"""
    x = 0
    y = 0
    #
    import math
    def square(self):
        """전달받은 수의 제곱을 반환한다."""
        return self.x * self.x

    def distance(self, point_a):
        """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
        return math.sqrt(square(self.x - point_a.x) + square(self.y - point_a.y))


point_1 = Coordinate()
point_2 = Coordinate()

point_1.x = -1
point_1.y = 2
point_2.x = 2
point_2.y = 3


print(point_1.distance(point_2))

# 인스턴스를 생성하면 가장 먼저 인스턴스 속성을 정의해야 한다. 이것을 초기화(initialization)라고 한다.

# __init__() 메서드로 인스턴스 초기화하기
# 우리가 Cake()과 같이 인스턴스화를 명령하면, 파이썬은 다음 두 단계에 걸쳐 인스턴스화를 수행한다.

# __new__() 메서드를 실행해 새 객체를 만든다.
# __init__() 메서드를 실행해 객체를 초기화한다.
# __new__ 메서드는 새 객체를 만드는 방법을 담은 메서드인데, 
# 파이썬이 기본으로 제공하기 때문에 여러분이 직접 정의할 필요는 없다.
#  __init__()는 새로 만들어진 객체의 속성을 초기화하는 메서드다. 
# 기본 제공되는 __init__() 메서드는 객체에 아무런 속성도 부여하지 않지만, 
# 여러분이 이 메서드를 직접 정의하면 인스턴스의 초기화 방법을 지시할 수 있다.

class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'
    # 
    def __init__(self, candles):
        """인스턴스를 초기화"""
        self.candles = candles
    #
    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.coat, '으로 덮여 있다.')
        print('초가', self.candles, '개 꽂혀 있다.')

cake_1 = Cake(12)   # 이제 초기값을 지정하여
cake_2 = Cake(100)  # 인스턴스화할 수 있다

print('케익 1:')
print('초 개수:', cake_1.candles)
print('케익 2:')
cake_2.describe()

class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'
    
    def __init__(self, topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.topping = topping   # 케익에 올린 토핑
        self.price = price      # 케익의 가격
        self.candles = candles  # 케익에 꽂은 초 개수
    
    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.coat, '으로 덮여 있다.')
        print(self.topping, '을 올려 장식했다.')
        print('가격은', self.price, '원이다.')
        print('초가', self.candles, '개 꽂혀 있다.')

cake_1 = Cake('눈사람 사탕', 10000)
cake_2 = Cake('한라봉', 9000, 8)

print('케익 1:')
cake_1.describe()

print('케익 2:')
cake_2.describe()


# 연습문제
class Coordinate:
    """좌표를 나타내는 클래스"""
    x = 0
    y = 0
    #
    import math

    def __init__(self, x=0, y=0):
        """인스턴스를 초기화한다."""
        self.x = x
        self.y = y

    def square(self, n):
        """전달받은 수의 제곱을 반환한다."""
        return n * n

    def distance(self, point_a):
        """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
        return math.sqrt(square(self.x - point_a.x) + square(self.y - point_a.y))


point_1 = Coordinate(-1, 2)
point_2 = Coordinate(y=3, x=2)
point_3 = Coordinate()
point_4 = Coordinate(10)

print(point_1.x, point_1.y)
print(point_2.x, point_2.y)
print(point_3.x, point_3.y)
print(point_4.x, point_4.y)

print(point_1.distance(point_2))
