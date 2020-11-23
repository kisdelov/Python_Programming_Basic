# 오류

# 구문 오류(syntax error), 실행시간 오류(runtime error), 논리 오류(logical error)로 분류할 수 있다. 

# 구문 오류: 프로그램의 문법이 잘못되어 기계어로 번역할 수 없을 때 발생하는 오류.
# 실행시간 오류: 프로그램의 문법에는 문제가 없으나, 명령을 실행할 수 없어 발생하는 오류.
# 특정 상황에서만 발생하는 실행시간 오류는 발견하고 대응하기가 어렵다.
# 논리 오류: 프로그램의 실행에는 문제가 없으나, 프로그램이 올바르게 동작하지 않는 오류. 발견하기가 어렵고 위험하다.

# 오류 메시지 
# SyntaxError: invalid syntax	                                구문 오류: 문법에 맞지 않다
# IndentationError: expected an indented block	                들여쓰기 오류: 들여쓰기를 해야 한다
# NameError: name ‘a’ is not defined	                        이름 오류: 이름 ‘a’가 정의되지 않았다
# TypeError: unsupported operand type(s) for +: ‘a’ and ‘b’	    유형 오류: 연산자 +가 피연자 유형 ‘a’와 ‘b’를 지원하지 않는다
# TypeError: must be ‘a’, not ‘b’	                            유형 오류: 유형이 ‘a’여야 하는데 ‘b’다
# TypeError: ‘int’ object is not callable	                    유형 오류: ‘int’ 유형 객체는 호출할 수 없다
# TypeError: f() takes 1 positional arguments but 2 were given	유형 오류: f() 함수는 인자 1개를 전달받는데 2개가 전달되었다
# TypeError: ‘str’ object does not support item assignment	    유형 오류: ‘str’ 유형 객체의 항목에 다른 값을 대입할 수 없다
# ValueError: invalid literal for int() with base 10: ‘a’	    값 오류: ‘a’는 int() 함수의 10진법으로 해석할 수 없다
# AttributeError: type object ‘int’ has no attribute ‘a’	    속성 오류: ‘int’ 유형 객체에는 ‘a’ 속성이 없다
# ZeroDivisionError: division by zero	                        영 나눗셈 오류: 영(0)으로 나눌 수 없다
# KeyError: ‘a’	                                                키 오류: (매핑 컬렉션에) ‘a’ 키가 없다

def median(data):
    """데이터의 중앙값을 반환한다."""
    sorted_data = sorted(data)
    median_value = sorted_data[int(len(sorted_data) / 2)]
    return median_value

print(median([10, 9, 4, 1, 5, 7]))

def 삼육구(n):
    """n에 숫자 '3', '6', '9' 중 하나 이상이 있을 경우 '짝'을,
    그렇지 않으면 n에 대응하는 숫자를 반환한다."""
    characters = str(n)
    found_3 = characters.find('3') != -1
    found_6 = characters.find('6') != -1
    found_9 = characters.find('9') != -1
    if found_3 or found_6 or found_9:
        return '짝'
    else:
        return str(n)

def test_삼육구():
    """삼육구() 함수가 올바른지 테스트한다."""
    if not(삼육구(1) == '1'):
        print('a')
        return False
    
    if not(삼육구(3) == '짝'):
        print('b')
        return False
    
    if not(삼육구(4) == '4'):
        print('c')
        return False
    
    if not(삼육구(6) == '짝'):
        print('d')
        return False
    
    if not(삼육구(9) == '짝'):
        print('e')
        return False
    
    return True

print()
print(삼육구(1))
print(삼육구(2))
print(삼육구(3))
print(삼육구(4))
print(삼육구(5))
print(삼육구(6))
print(삼육구(7))
print(삼육구(8))
print(삼육구(9))
print(삼육구(10))
print(test_삼육구())

# 예외(exception)란 프로그램이 정상적으로 실행될 수 없는 상황을 뜻한다.
# 프로그램 안에 예외 상황에 대한 대응책을 마련해두어야 한다. 이를 예외 처리(exception handling)라고 한다.

# if 문으로 예외 처리하기

# 데이터 입력
# print('0이 아닌 정수를 입력해 주세요:', end=' ')
# user_number = int(input())

# # 결과 출력
# print(1 / user_number)

# # 데이터 입력
# print('0이 아닌 정수를 입력해 주세요:', end=' ')
# user_number = int(input())

# # ❶ 예외 처리: 입력값이 0인 경우 프로그램 종료
# if user_number == 0:
#     print('0으로 나눌 수 없습니다.')
#     exit()   # ❷ 프로그램 종료

# # 결과 출력
# print(1 / user_number)

# 데이터 입력
# print('0이 아닌 정수를 입력해 주세요:', end=' ')
# user_string = input()

# # 예외 처리: 입력값이 정수가 아닌 경우 프로그램 종료
# if not user_string.isnumeric():
#     print(user_string, '은 정수가 아닙니다.')
#     exit()   # 프로그램 종료

# # 입력값(문자열)을 정수로 변환
# user_number = int(user_string)

# # 예외 처리: 입력값이 0인 경우 프로그램 종료
# if user_number == 0:
#     print('0으로 나눌 수 없습니다.')
#     exit()   # 프로그램 종료

# # 결과 출력
# print(1 / user_number)

# try 문과 except 절

# # ❶ try 블록에 예외가 일어날 수 있는 코드를 기술한다.
# try:
#     print('0이 아닌 정수를 입력해 주세요:', end=' ')
#     user_number = int(input())
#     print(1 / user_number)
# # ❷ 처리해야 할 예외의 이름과 처리방법을 except 블록에 기술한다.
# except ZeroDivisionError:  # 0으로 나누는 오류 처리
#     print('0으로 나눌 수 없습니다.')
# except ValueError:         # int 유형이 될 수 없는 문자열의 오류 처리
#     print('입력한 값은 정수가 아닙니다.')

# while True:
#     try:
#         print('0이 아닌 정수를 입력해 주세요:', end=' ')
#         user_number = int(input())
#         result = 1 / user_number
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#     except ValueError:
#         print('입력한 값은 정수가 아닙니다.')
    
#     # 예외가 발생하지 않은 경우에만 실행
#     else:
#         print(result)  # 결과를 출력하고
#         break          # 반복을 빠져나간다

# # 연습문제
# print('첫번째 수를 입력하시오: ', end='')
# number1 = int(input())
# print('두번째 수를 입력하시오: ', end='')
# number2 = int(input())

# add = number1 + number2
# subtract = number1 - number2
# multiply = number1 * number2
# try:
#     divide = number1 / number2
# except ZeroDivisionError:
#     divide = 'None'

# print(number1, '+', number2, '=', add)
# print(number1, '-', number2, '=', subtract)
# print(number1, '*', number2, '=', multiply)
# print(number1, '/', number2, '=', divide)

# https://python.bakyeono.net/img/img-9-4.png 예외 종류

class DoorException(Exception):
    """문과 관련된 예외"""
    pass

class DoorOpenedException(DoorException):
    """문 열림 예외"""
    pass

class DoorClosedException(DoorException):
    """문 닫힘 예외"""
    pass

# 연습 문제

# class AcountException(Exception):
#     """계좌와 관련된 예외"""
#     pass

# class AcountBalanceException(AcountException):
#     """계좌 잔고 예외"""
#     pass

# class FrozenAccountException(AcountException):
#     """동결 계좌 예외"""
#     pass

# class InvalidTransctionException(AcountException):
#     """잘못된 입출금 예외"""
#     pass

# raise ZeroDivisionError('0으로 나눌 수 없음')


class Door:
    """문을 나타내는 클래스"""
    def __init__(self):
        self.is_opened = True  # 문이 열려있는지를 나타내는 상태

    def open(self):
        # ❶ 문이 이미 열린 경우, 예외를 일으킨다
        if self.is_opened:
            raise DoorOpenedException('문이 이미 열려 있음')
        # 그렇지 않다면, 문을 연다
        else:
            print('문을 엽니다.')
            self.is_opened = True

    def close(self):
        # 문이 이미 닫힌 경우, 예외를 일으킨다
        if not self.is_opened:
            raise DoorClosedException('문이 이미 닫혀 있음')
        # 그렇지 않다면, 문을 닫는다
        else:
            print('문을 닫습니다.')
            self.is_opened = False

door = Door()  # 문 인스턴스 생성
door.close()   # 문 닫기
door.open()    # 문 열기
# door.open()    # 문 열린 상태에서 문 열기

# 연습 문제

class AcountException(Exception):
    """계좌와 관련된 예외"""
    pass

class AcountBalanceException(AcountException):
    """계좌 잔고 예외"""
    pass

class FrozenAccountException(AcountException):
    """동결 계좌 예외"""
    pass

class InvalidTransctionException(AcountException):
    """잘못된 입출금 예외"""
    pass

class Account():
    """은행 계좌"""
    def __init__(self, balance, is_frozen):
        """인스턴스를 초기화한다."""
        self.balance = balance      # 계좌 잔액
        self.is_frozen = is_frozen  # 계좌 동결 여부
    
    def check(self):
        """계좌의 잔고를 조회한다."""
        print('계좌 잔액은', self.balance, '원 입니다.')
    
    def deposit(self, amount):
        """계좌에 amount 만큼의 금액을 입금한다."""
        if self.is_frozen:
            raise FrozenAccountException('계좌가 동결 상태입니다.')
        elif amount <= 0:
            raise InvalidTransctionException('0 이하의 액수는 입금할 수 없습니다.')
        else:
            self.balance += amount
            self.check()
    
    def withdraw(self, amount):
        """계좌에서 amount 만큼의 금액을 인출한다."""
        # if self.is_frozen:
        #     raise FrozenAccountException('계좌가 동결 상태입니다.')
        # elif self.balance < amount:
        #     raise AcountBalanceException('계좌 잔고가 부족합니다.')
        # elif amount <= 0:
        #     raise InvalidTransctionException('0 이하의 액수는 출금할 수 없습니다.')
        # else:
        #     self.balance -= amount
        #     self.check()
        assert self.is_frozen, '계좌가 동결 상태입니다.'
        assert self.balance < amount, '계좌 잔고가 부족합니다.'
        assert amount <= 0, '0 이하의 액수는 출금할 수 없습니다.'
        self.balance -= amount
        self.check()

acount = Account(100000, False)
acount.check()
acount.deposit(100000)
acount.withdraw(100000)
acount.withdraw(100001)

# assert 문: 단언하기


