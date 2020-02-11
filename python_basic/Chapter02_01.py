# chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start')
print("Python Start")
print('''python Start''')
print("""python Start""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션

print('welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Ptyhon', file=sys.stdout)
print()

# format 사용(d 정수 : 3, s 문자열 : 'python', f 실수 : 3.1445)
print('%s %s' % ('Fucking', 'H'))
print('{} {}'.format('one', 'two')) #format에 구애받지 않는다.
print('{1} {0}'.format('one', 'two')) #괄호안에 순서를 지정
print()

# %s
print('%10s' % ('nice')) #10개의 자리수 중에 문자열을 출력하고 나머지는 공백
print('{:>10}'.format('nice'))

print('%-10s' % ('nice')) #음수일 경우 나머지 부분을 왼쪽부터 채운다
print('{:10}'.format('nice')) #생략하면 왼쪽부터

print('{:_>10}'.format('nice')) #한글자로 채우기
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) #n개만큼 절삭, .이 없으면 다 출력
print('{:10.5}'.format('pythonstudy')) #공간은 10개를 갖고 있지만, 5개에서 절삭

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42)) #정수일 경우 {}에 d를 추가

# %f
print('%f' % (3.141231524351))
print('{:f}'.format(3.141231524351))

print('%06.2f' % (3.1415926535892359)) #총 자리수는 6이고, 소수부는 2자리, 나머지 빈공간은 0으로 채운다
print('{:06.2f}'.format(3.1415926535892359))
