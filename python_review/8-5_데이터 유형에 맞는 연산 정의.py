# 데이터 유형에 맞는 연산 정의하기

# 인터페이스(interface, 접점)는 한 대상이 다른 대상과 맞닿는 면이다. 
# 전자 제품이나 소프트웨어처럼 내부 구조가 복잡한 제품에서는 인터페이스가 사용자가 제품을 사용하는 방법이 된다. 

# 클래스를 정의할 때, 클래스의 속성을 감추어두고 연산자와 메서드를 인터페이스로 제공하는 방법을 캡슐화(encapsulation)라고 부른다. 
# 부동 소수점 수를 직접 구현해 실수 연산을 수행하려면 부호·가수부·지수부 등 여러 속성을 정의하고 조작해야 할 것이다. 

class FruitJuice():
    """과일 주스를 나타내는 클래스"""
    valid_fruits = {'귤', '복숭아', '청포도', '딸기', '사과'}  # 넣을 수 있는 과일
    
    def __init__(self):
        """인스턴스를 초기화한다."""
        self.ingredients = []   # 주스에 들어가는 재료
    
    def add_ingredient(self, ingredient):
        """재료(ingredient)를 이 주스에 추가한다."""
        if ingredient in self.valid_fruits:
            self.ingredients.append(ingredient)
        else:
            print(ingredient, '는 과일 주스에 넣을 수 없습니다.')
    
    def describe(self):
        """이 주스에 관한 정보를 화면에 출력한다."""
        print('이 주스에는', len(self.ingredients), '개의 재료가 들어 있습니다.')
        print('넣은 재료:', end=' ')
        for ingredient in self.ingredients:
            print(ingredient, end=', ')

juice_1 = FruitJuice()
juice_1.add_ingredient('청포도')  # 재료 추가하기
juice_1.add_ingredient('복숭아')  # 재료 추가하기
juice_1.add_ingredient('도라지')  # 잘못된 재료 추가하기
juice_1.describe()

# 비공개 속성

class FruitJuice():
    """과일 주스를 나타내는 클래스"""
    _valid_fruits = {'귤', '복숭아', '청포도', '딸기', '사과'}  # 넣을 수 있는 과일
    
    def __init__(self):
        """인스턴스를 초기화한다."""
        self._ingredients = []   # 주스에 들어가는 재료
    
    def add_ingredient(self, ingredient):
        """재료(ingredient)를 이 주스에 추가한다."""
        if ingredient in self._valid_fruits:
            self._ingredients.append(ingredient)
        else:
            print(ingredient, '는 과일 주스에 넣을 수 없습니다.')
    
    def describe(self):
        """이 주스에 관한 정보를 화면에 출력한다."""
        print('이 주스에는', len(self._ingredients), '개의 재료가 들어 있습니다.')
        print('넣은 재료:', end=' ')
        for ingredient in self._ingredients:
            print(ingredient, end=', ')


# 연습문제

import random

class Dice():
    """주사위를 나타내는 클래스"""

    def __init__(self, sides):
        """인스턴스를 초기화한다."""
        self._sides = sides   # 주사위 면의 수
    
    def top(self):
        """현재 나온 면을 반환한다."""
        print('처음 나온면 : {}'.format(random.randint(1, self._sides)))

    def role(self):
        """새로 나온 면을 반환한다."""
        print('다시 굴리기 : {}'.format(random.randint(1, self._sides)))
    
dice_4 = Dice(4)      # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
dice_4.top()
dice_4.role()
dice_4.role()

dice_100 = Dice(100)  # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
dice_100.top()
dice_100.role()
dice_100.role()

# 연산자의 동작 정의하기

class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):              # ❶
        """인스턴스를 초기화한다."""
        self._taste = taste      # 맛
        self._calorie = calorie  # 칼로리
    
    def to_string(self):                             # ❷
        """이 음식을 표현하는 문자열을 반환한다."""
        return str(self._taste) + '만큼 맛있고, ' + str(self._calorie) + '만큼 든든한 음식'
    
    def add(self, other):                            # ❸
        """이 음식(self)과 다른 음식(other)을 더한
        새 음식을 반환한다."""
        taste = self._taste + other._taste           # 두 음식의 맛을 더한다
        calorie = self._calorie + other._calorie     # 두 음식의 칼로리를 더한다
        return Food(taste, calorie)                  # 새 음식 인스턴스를 생성하여 반환한다

food1 = Food(7, 85)
print()
print(food1.to_string())
food2 = Food(12, 266)
print(food2.to_string())
food3 = food1.add(food2)
print(food3.to_string())

# 이중 밑줄 메서드

class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self._taste = taste      # 맛
        self._calorie = calorie  # 칼로리
    
    def __str__(self):           # ❶ to_string() 메서드의 이름을 __str__()로 수정했다
        """이 음식을 표현하는 문자열을 반환한다."""
        return str(self._taste) + '만큼 맛있고, ' + str(self._calorie) + '만큼 든든한 음식'
    
    def __add__(self, other):    # ❷ add() 메서드의 이름을 __add__()로 수정했다
        """이 음식(self)과 다른 음식(other)을 더한
        새 음식을 반환한다."""
        taste = self._taste + other._taste           # 두 음식의 맛을 더한다
        calorie = self._calorie + other._calorie     # 두 음식의 칼로리를 더한다
        return Food(taste, calorie)                  # 새 음식 인스턴스를 생성하여 반환한다

    def __lt__(self, other):
        """음식 맛을 비교하고, 같다면 칼로리가 적은 것을 우위"""
        if self._taste < other._taste:
            return True
        elif self._taste == other._taste:
            if self._calorie > other._calorie:
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        """음식 맛을 비교하고, 같다면 칼로리가 적은 것을 우위"""
        if self._taste > other._taste:
            return True
        elif self._taste == other._taste:
            if self._calorie <= other._calorie:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        """음식 맛을 비교하고, 같다면 칼로리가 적은 것을 우위"""
        if self._taste == other._taste:
            if self._calorie == other._calorie:
                return True
        else:
            return False


print(Food(7, 85) + Food(12, 266))
strawberry = Food(9, 32)
potato = Food(6, 66)
sweet_potato = Food(12, 131)
pizza = Food(13, 266)
print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= pizza)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)


# 메서드	                호출되는 연산	    기능
# __init__(self)	        인스턴스화	        인스턴스 초기화
# __abs__(self)	            abs(self)	        절대값 계산
# __add__(self, other)	    self + other	    덧셈 계산
# __sub__(self, other)	    self - other	    뺄셈 계산
# __mul__(self, other)	    self * other	    곱셈 계산
# __truediv__(self, other)	self / other	    나눗셈 계산
# __pow__(self, other)	    self ** other	    거듭제곱 계산
# __floordiv__(self, other)	self // other	    몫 계산
# __mod__(self, other)	    self % other	    나머지 계산
# __lt__(self, other)	    self < other	    미만 계산
# __gt__(self, other)	    self > other	    초과 계산
# __le__(self, other)	    self <= other	    이하 계산
# __ge__(self, other)	    self >= other	    이상 계산
# __eq__(self, other)	    self == other	    동등 계산
# __ne__(self, other)	    self != other	    부등 계산
# __repr__(self)	        repr(self)	        객체를 식별할 수 있는 문자열 반환
# __str__(self)	            str(self)	        객체에 대응하는 문자열 반환
# __int__(self)	            int(self)	        객체에 대응하는 정수 반환
# __float__(self)	        float(self)	        객체에 대응하는 실수 반환
# __bool__(self)	        bool(self)	        객체에 대응하는 불리언 값 반환