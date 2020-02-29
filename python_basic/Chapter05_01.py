# Chapter05-01
# 코드의 재사용성, 함수 단위 개발 설계 용이, 오류 검정 용이 등
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code 궁금해

# 예제 1


def first_func(w):
    print("Hello,", w)


word = "Goodboy"

first_func(word)

# 예제 2


def return_func(w):
    value = "Hello, " + str(w)
    return value


x = return_func("Goodboy2")
print(x)

# 예제 3 (다중반환)


def func_mu1(i):
    y1 = i*10
    y2 = i*20
    y3 = i*30
    return y1, y2, y3


x, y, z = func_mu1(10)

print(x, y, z)

# 튜플 리턴


def func_mu2(i):
    y1 = i*10
    y2 = i*20
    y3 = i*30
    return (y1, y2, y3)


q = func_mu2(20)

print(type(q), q, list(q))

# 리스트 리턴


def func_mu3(i):
    y1 = i*10
    y2 = i*20
    y3 = i*30
    return [y1, y2, y3]


p = func_mu2(30)

print(type(p), p, set(p))

# 딕셔너리 리턴


def func_mu3(i):
    y1 = i*10
    y2 = i*20
    y3 = i*30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mu3(30)

print(type(d), d, d.get('v1'), d.items(), d.keys())

# 중요
# *args, **kwargs

# *args(언팩킹)


def args_func(*args):  # 매개변수 명 자유
    for i, v in enumerate(args):
        print("Result : {}".format(i), v)
    print('-----')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(언팩킹)


def kwargs_func(**kwargs):  # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho', sendSMS=True)

# 전체 혼합
def example(args_1, args_2, *args_3, **args_4):
    print(args_1, args_2, args_3, args_4)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

# 중첩함수 : 함수 안에 함수 - 호출이 되지 않는다~

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num+100)

nested_func(100)

# 실행불가
# func_in_func() 부모 함수를 호출하지 않으면 정의되지 않는다










