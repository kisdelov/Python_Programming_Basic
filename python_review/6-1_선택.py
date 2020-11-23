# 선택

# 여러 선택지 중 하나 고르기

# if 문

# print('오늘 낮의 날씨를 입력해주세요:')
# 날씨 = input()

# if 날씨 == '비':
#     print('집콕')
# if 날씨 == '맑음':
#     print('나가기')
    
# if 문 함수에서 활용

def 절대값(n):
    """수 n을 입력받아, 절대값을 반환한다.
    """
    if n >= 0 : # n이 0 이상이면 n을 반환
        return n
    if n < 0 : # n이 0 미만이면 -n을 반환
        return -n
    
print('10의 절대값 :', 절대값(10))
print('-5의 절대값 :', 절대값(-5))

# pass 문

def 절대값(n):
    """수 n을 입력받아, 절대값을 반환한다.
    """
    if n >= 0 : # n이 0 이상이면 n을 반환
        pass # 조건이 참이어도 아무 것도 실행하지 않는다.
    if n < 0 : # n이 0 미만이면 -n을 반환
        return -n

# elif 문 : 선택지가 여러 개일 때

# print('일요일 낮의 기온을 입력해주세요:')
# 기온 = float(input())  # 입력받은 기온을 실수로 변환하자

# if 28.0 <= 기온:    # ❶ 첫 번째 선택지
#     print('바닷가에서 더위를 피하자.')

# elif 16.0 <= 기온:  # ❷ 위 조건이 거짓일 때 검사
#     print('공원에서 스케이트보드를 타자.')

# elif 8.0 <= 기온:   # ❸ 위 조건이 거짓일 때 검사
#     print('도서관에서 책을 읽자.')

# else:               # ❹ 모든 조건이 거짓일 때 실행
#     print('집에서 프로그램을 만들자.')

# 조건부 식

# 가격 = 1000 if 요일 == '월요일' else 2500

# if 요일 == '월요일':
#     가격 = 1000  # ❶ if 문의 본문에 대입문이 하나 필요하고...
# else:
#     가격 = 2500  # ❷ else 절의 본문에도 대입문이 하나 필요하다
    


# 할인 가격

def price(n):
    if n < 10:
        return print('총 지불 가격은 {}원 입니다.'.format(n * 100))
    elif n >= 10 and n < 30:
        return print('총 지불 가격은 {}원 입니다.'.format(n * 95))
    elif n >= 30 and n < 100:
        return print('총 지불 가격은 {}원 입니다.'.format(n * 90))
    else:
        return print('총 지불 가격은 {}원 입니다.'.format(n * 85))
    
price(20)

def is_leap_year(y):
    if (y%4) == 0 :
        if (y%100) == 0:
            if (y%400) == 0:
                return True
            return False
        return True
    
print(is_leap_year(1996))

def days_in_month(y, m):
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    elif m in [1, 3, 5, 7, 8, 10, 12] :
        return 31
    elif m in [4, 6, 9, 11] :
        return 30
    
print(days_in_month(1996, 2))
    
    
def Bmi_1(t, w):
    return w/(t*t)
def Bmi_2(bmi):
    if bmi < 18.5:
        print('저체중입니다.')
    elif bmi >= 18.5 and bmi < 23:
        print('정상입니다.')
    elif bmi >= 23 and bmi > 25:
        print('과체중입니다.')
    else :
        print('비만입니다.')


print('키를 입력하세요(m) :', end = ' ') 
t = float(input())
print('몸무게를 입력하세요(kg) :', end = ' ') 
w = float(input())

Bmi_2(Bmi_1(t, w))

def absolute_number(n):
    return n if n > 0 else -n

print(absolute_number(-100))