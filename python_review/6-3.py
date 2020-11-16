# 단축 평가

# 단축 평가(short-circuit evaluation)란 계산을 진행하는 도중에 결과가 이미 확정된 경우, 나머지 계산 과정을 생략하는 것이다. and 연산과 or 연산은 연산의 특성상 단축 평가를 할 수 있다. 컴퓨터의 계산 자원을 절약하기 위해 파이썬을 포함한 대부분의 프로그래밍 언어는 이 두 연산에 단축 평가를 적용하고 있다.

def 홀짝(n):
    """n이 홀수인지 짝수인지를 화면에 출력한다."""
    (n % 2 == 0) and print(n, '은 짝수입니다.')
    (n % 2 == 0) or print(n, '은 홀수입니다.')

홀짝(10)
홀짝(11)

# 재귀
def 자연수(n, m):
    """수 n을 출력하고, 1 더한 수가 m보다 작으면 그 수도 출력한다."""
    print(n)
    if n + 1 < m:
        자연수(n + 1, m)

자연수(4, 8)

def n번째_피보나치_수(n):
    """n번째 피보나치 수를 반환한다."""
    if n == 1:     # 첫 번째 피보나치 수는 1
        return 1
    elif n == 2:   # 두 번째 피보나치 수는 1
        return 1
    else:          # 그 후의 피보나치 수
        return n번째_피보나치_수(n - 1) + n번째_피보나치_수(n - 2)

# 1번째부터 11번째 피보나치 수까지 출력
for n in range(1, 12):
    print(n번째_피보나치_수(n), end=' ')