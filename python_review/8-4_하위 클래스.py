# 하위 클래스 정의하기

# class B(A):
#     """A 클래스의 하위 클래스인 B 클래스"""
#     이 하위 클래스의 공용 속성

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

class ChocolateCake(Cake):
    """초콜릿 케이크를 나타내는 클래스"""
    coat = '초콜릿' # 상위 클래스에 정의된 속성은 하위 클래스에서 고쳐 정의할 수 있다. 이를 재정의(override)라고 한다.
    cacao_percent = 32.0
    
class IceCreamCake(Cake):
    """아이스크림 케익을 나타내는 클래스."""
    coat = '아이스크림'
    flavor = '정해지지 않은 맛'
    
    def __init__(self, flavor, topping, price, candles=0):  # ❶
        """인스턴스를 초기화한다."""
        self.flavor = flavor  # 아이스크림의 맛             # ❷
        super().__init__(topping, price, candles)     # ❸

print(ChocolateCake.coat)           # ❶ 재정의한 클래스 속성
print(ChocolateCake.cacao_percent)  # ❷ 추가한 클래스 속성

# ❸ 상위 클래스 Cake의 __init__() 메서드와 __describe__() 메서드 이용하기
chocolate_cake_1 = ChocolateCake('이슬', 12000)
chocolate_cake_1.describe()

ice_cream_cake_1 = IceCreamCake('바닐라맛', '쿠키 인형', 12000)
ice_cream_cake_1.describe()

# 클래스의 하위 클래스를 정의할 수 있다.
# 하위 클래스는 상위 클래스의 속성을 사용할 수 있고, 자신만의 속성을 가질 수도 있다.
# 하위 클래스에서 상위 클래스를 가리킬 때 super() 함수를 사용할 수 있다.

# 클래스의 계층 살펴보기

class FruitIceCreamCake(IceCreamCake):
    """과일 아이스크림 케익을 나타내는 클래스."""
    def __init__(self, fruit_percent, flavor, topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.fruit_percent = fruit_percent  # 과일 함량 (퍼센트)
        super().__init__(flavor, topping, price, candles)  # IceCreamCake.__init__()
    
    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.flavor, '맛이다.')
        print('이 케익은', self.fruit_percent, '% 과일이 함유돼 있다.')
        super().describe()

fruit_ice_cream_cake_1 = FruitIceCreamCake('50', '딸기', '쿠키 인형', 12000)
print()
fruit_ice_cream_cake_1.describe()

# issubclass() 함수로 어떤 클래스가 다른 클래스의 하위 클래스인지 확인할 수 있다.
# 모든 클래스는 object 클래스의 하위 클래스다.
# 하위 클래스에서 속성을 읽을 때, 먼저 자신의 이름공간에서 찾고 없으면 상위 클래스에서 찾는다.

#  다중 상속
class CakePiece:
    """조각 케익"""
    size = 1 / 8
    calorie = 200

class CheeseCake(Cake):
    """치즈 케익"""
    body = '치즈'
    calorie = 1600

class CheeseCakePiece(CakePiece, CheeseCake):  # 상속할 클래스를 괄호 안에 나열한다
    """치즈 조각 케익"""
    pass  # 추가로 정의할 속성이 없으면 pass 문으로 비워 둔다

print()
print('body:', CheeseCakePiece.body)        # CheeseCake의 속성을 읽는다
print('size:', CheeseCakePiece.size)        # CakePiece의 속성을 읽는다
print('calorie:', CheeseCakePiece.calorie)  # CakePiece의 속성을 읽는다

# 믹스인

# 클래스 중에는 멤버 변수 없이 모든 속성이 메서드로만 이루어진 특별한 클래스가 있는데, 믹스인(mixin)이라고 부른다. 
# 믹스인은 다양한 클래스에서 공통적으로 사용할 수 있는 메서드들을 묶어둔 클래스다. 
# 클래스를 정의할 때 필요한 믹스인을 다중 상속하여 섞어 넣어(mix in), 믹스인의 메서드를 이용할 수 있다. 
# 믹스인에는 변화하는 상태가 존재하지 않고 오직 메서드만 있기 때문에 다중 상속을 하더라도 비교적 안전하다.

# 연습문제

# Shape: 도형을 나타내는 클래스
# 클래스 메서드 describe(): “이 도형은 3 개의 변을 갖고 있습니다.”와 같이 이 도형의 특징을 화면에 출력한다. 
# 변의 개수는 self.sides 속성을 읽어 구한다.
# Triangle: 삼각형을 나타내는 클래스
# Shape 클래스를 상속
# 클래스 속성 sides: 변의 개수를 나타내는 속성. 3으로 고정
# Rectangle: 사각형을 나타내는 클래스
# Shape 클래스를 상속
# 클래스 속성 sides: 변의 개수를 나타내는 속성. 4로 고정

import math

class Coordinate:
    """좌표를 나타내는 클래스"""


    def __init__(self, x=0, y=0):
        """인스턴스를 초기화한다."""
        self.x = x
        self.y = y

    def square(self, n):
        """전달받은 수의 제곱을 반환한다."""
        return n * n

    def distance(self, point_a):
        """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
        return math.sqrt(self.square(self.x - point_a.x) + self.square(self.y - point_a.y))

class Shape :
    """도형을 나타내는 클래스"""
    sides = 0

    def describe(self):
        print('이 도형은 {}의 변을 갖고 있습니다.'.format(self.sides))

class Triangle(Shape, Coordinate):
    """삼각형을 나타내는 클래스"""
    sides = 3

    def __init__(self, point_a=Coordinate(), point_b=Coordinate(), point_c=Coordinate()):
        """인스턴스를 초기화한다."""
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def circumference(self): 
        """삼각형의 둘레를 계산하여 반환한다."""
        return self.point_a.distance(self.point_b) + self.point_b.distance(self.point_c) + self.point_c.distance(self.point_a)
    
class Rectangle(Shape, Coordinate):
    """사각형을 나타내는 클래스"""
    sides = 4

    def __init__(self, point_a=Coordinate(), point_b=Coordinate(), point_c=Coordinate(), point_d=Coordinate()):
        """인스턴스를 초기화한다."""
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def circumference(self): 
        """삼각형의 둘레를 계산하여 반환한다."""
        return self.point_a.distance(self.point_b) + self.point_b.distance(self.point_c) + self.point_c.distance(self.point_d) + self.point_d.distance(self.point_a)

shapes = [Triangle(), Rectangle()] 

for shape in shapes: 
    shape.describe()

print()

shapes = [
    Triangle(Coordinate(0, 0), Coordinate(3, 0), Coordinate(3, 4)),
    Rectangle(Coordinate(2, 2), Coordinate(6, 2), Coordinate(6, 6), Coordinate(2, 6)),
]
for shape in shapes:
    shape.describe()
    print('둘레:', shape.circumference())
