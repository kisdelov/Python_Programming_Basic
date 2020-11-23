# 챕터 3 함수

# 함수 정의
# def order() :
#     print('주문하실 음료를 알려주세요')
#     drink = input()
#     print(drink, '주문 감사합니다.')

# order()

# def 정수() :
#     """
#     함수가 하는 일을 설명하는 곳으로 독스트링(docstring)이라고 한다.
#     정수를 입력하고 해당 수의 절대값을 알려주는 함수
#     """
#     print('정수를 입력해')
#     절대 = int(input())
#     print('{}의 절대값 : {}'.format(절대, abs(절대)))

# 정수()
# print(정수.__doc__)

# 전역변수, 지역변수

def divide(number, by=2) :
    """
    number/by by 기본설정 2
    """
    return number/by

print('{}'.format(divide(12,3)))

# 람다함수
# lambda 매개변수 : 반환값