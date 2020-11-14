# 언패킹과 패킹

# 여러 개의 데이터를 컬렉션으로 묶어 변수에 대입하는 것을 패킹(packing, 싸기)이라고 부른다.

numbers = 1, 2, 3, 4, 5  # 패킹
a, b, c, d, e = numbers  # 언패킹
a, b, c, d, _ = numbers  # 언패킹(마지막은 필요 없을 경우)

# 자리를 메우는 변수의 이름은 관례적으로 밑줄 기호 하나(_)로 한다.

# 남은 요소 대입받기
# 대입문에서 좌변의 변수 중 하나에 별 기호(*)를 붙이면, 남은 요소 전체를 리스트에 담아 대입한다.

a, b, c, *rest = numbers  # 언패킹(남은 요소 4, 5는 rest에 대입)

# 시퀀스를 함수 매개변수에 전달하기


def date_to_string(y, m, d):
    """
    년(y), 월(m), 일(d)을 입력받아,
    'y년 m월 d일' 형태의 문자열을 반환한다.
    """
    return str(y) + '년 ' + str(m) + '월 ' + str(d) + '일'


date = 1996, 5, 23
print(date_to_string(*date))  # *을 붙이면 풀어서 전달

# 함수에서 임의의 개수의 데이터를 전달받기

def mean(*args):
    """여러 개의 수를 전달받아 산술평균을 계산한다.
    """
    return sum(args)/len(args)

print(mean(1,2,3,4,5,6,7,8,9))
print(mean(*numbers))

# 필수 매개변수와 나머지 매개변수 정의하기

def 가격계산(할인율, *구매가_목록):
    """구매가 목록을 합산하고 할인율을 반영해 가격을 계산한다.
    """
    return (1-할인율) * sum(구매가_목록)

print(가격계산(0.25, 100))
print(가격계산(0.25, 100, 2000, 30000, 40000))

def gap(*args) : 
    """인자 중 가장 큰 수와 가장 작은 수의 차이를 반환한다.
    """
    return max(args) - min(args)

print(gap(100))
print(gap(10, 20, 30, 40))
ages = [19, 16, 24, 19, 23]
print(gap(*ages))

# 함수의 매개변수와 매핑 패킹·언패킹

dates = {'y' : 1996, 'm' : 5, 'd' : 23}
print(date_to_string(**dates)) # 매핑의 키와 함수의 매개변수가 서로 이름이 같다면 **를 표기하여 언패킹이 가능

# 함수에서 다양한 이름의 데이터를 전달받기

def date_to_string2(y, m, d, **kwargs):
    """
    년(y), 월(m), 일(d)을 입력받아,
    'y년 m월 d일' 형태의 문자열을 반환한다.
    """
    date_string = str(y) + '년 ' + str(m) + '월 ' + str(d) + '일'
    
    # 시(h) 매개변수가 전달된 경우 문자열에 덧붙인다
    date_string += ' ' + str(kwargs.get('h')) + '시'
    
    return date_string

print(date_to_string2(**dates, h = 12))

def concatenate(*args, **kwargs):
    """문자열을 전달받아 구분자를 각 문자열 사이에 끼워넣어 반환
    """
    print((kwargs.get('seperator')).join(args))

concatenate('가난하다고', '해서', '외로움을', '모르겠는가', seperator = ' ')
concatenate(*'월화수목금토일 ', seperator = '요일 ')