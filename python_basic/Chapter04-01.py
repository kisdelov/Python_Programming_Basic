# Chapter04-01
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1,2,3,4,..], (1,2,3,4...) ...
print(type(False)) # 0, "", [], (), {} ...

# 예1

if True:
    print('Good')

if False:
    print('Bad')

# 예2
if True:
    print('Bad!')
else:
    print('Good!')
print()

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양변이 같을 때 참
print(x == y)

# 양변이 다를 때 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 예3
city = ""
if city:
    print("You are in :", city)
else:
    print("Please enter your city")

# 예4
city2 = "Seoul"
if city2:
    print("You are in :", city2)
else:
    print("Please enter your city")



