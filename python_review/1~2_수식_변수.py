# 챕터 1 수식

p1 = ((-32)+96)/(12/3)
p2 = (3*4-(((-27)+67)/4))**8
p3 = (((512+1968-432)/2**4)+128)

print(p1)
print(p2)
print(p3)

# 알아두기
# abs() : 수의 절대값
# round() : 소수를 반올림
# math.sqrt() : 수의 제곱근
# math. 으로 시작하는 함수 사용 전, import math를 실행

import math

hundred = abs(-100)
three = math.sqrt(3)

print('{} {}'.format(hundred, three))
print()

# 챕터 2 변수

x = 16
y = (8*x)**2-(2*x)+2
print(y)

# 변수 삭제는 del(변수)

print('첫 번째 정수를 입력')
정수1 = int(input())
print('두 번째 정수를 입력')
정수2 = int(input())

print('{} + {} = {}'.format(정수1, 정수2, 정수1+정수2))
print('{} - {} = {}'.format(정수1, 정수2, 정수1-정수2))
print('{} * {} = {}'.format(정수1, 정수2, 정수1*정수2))
print('{} / {} = {}'.format(정수1, 정수2, 정수1/정수2))

