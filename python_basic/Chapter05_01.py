# Chapter05-01
# 코드의 재사용성, 함수 단위 개발 설계 용이, 오류 검정 용이 등
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code

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
