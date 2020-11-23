# 수학 도구 상자

# math 모듈은 다양한 수학 도구를 담은 도구 상자다. 제곱근, 로그, 계승, 삼각함수 등 수학 하면 쉽게 떠올릴 수 있는 다양한 함수와 원주율과 자연상수 같은 중요한 상수가 정의되어 있다.

# 함수	            값 또는 기능
# math.factorial(x)	x의 계승(팩토리얼)
# math.gcd(a, b)	a와 b의 최대공약수
# math.floor(x)	    x의 소수점 아래를 버린다
# math.ceil(x)	    x의 소수점 아래를 올린다
# math.pow(x, y)	x의 y 승
# math.sqrt(x)	    x의 제곱근
# math.log(x, base)	base를 밑으로 하는 x의 로그
# math.sin(x)	    x 라디안의 사인
# math.cos(x)	    x 라디안의 코사인
# math.tan(x)	    x 라디안의 탄젠트
# math.degrees(x)	x 라디안을 도(°) 단위로 변환한다
# math.radians(x)	x 도(°)를 라디안 단위로 변환한다

# 상수	        값
# math.pi	    원주율 (3.141592653589793...)
# math.e	    자연상수 (2.718281828459045...)
# math.inf	    양의 무한대

# fractions 모듈에는 분수를 나타내는 fractions.Fraction 클래스가 정의되어 있다. fractions 모듈을 사용할 때는 변수에 모듈 전체 대신 Fraction 클래스만 임포트하는 편이 편리하다.

from fractions import Fraction   # Fraction 클래스 임포트
print(Fraction(2, 3) * 5)

# 난수란 정해지지 않은 임의의 수로, 프로그래밍에서는 코드를 평가할 때마다 임의의 값으로 평가되는 데이터를 가리킨다.

# 함수	                값 또는 기능
# random.randint(a, b)	a 이상 b 이하의 임의의 정수
# random.random()	    0 이상 1 미만의 임의의 실수
# random.choice(seq)	시퀀스에서 요소 하나를 무작위로 선택한다
# random.sample(seq, k)	시퀀스에서 요소 k 개를 무작위로 선택한다
# random.shuffle(seq)	시퀀스를 무작위로 섞는다
# random.seed(a)	    난수의 씨앗 값을 a로 설정한다

# 씨앗 값 설정
# 시뮬레이션을 진행할 때 난수가 발생하는 순서를 통제해야 할 때가 있다. random.seed() 함수로 난수가 발생하는 씨앗 값을 설정할 수 있다. 동일한 씨앗 값을 설정하면 난수의 발생 순서가 동일하게 재현된다.

# tertools 모듈은 시퀀스의 요소를 조합해 곱집합·순열·조합을 구하는 함수를 제공한다. 이 연산들은 확률 계산에 유용하게 사용될 수 있다. 

# 함수	                                            값 또는 기능
# itertools.product(seq1, ...)	                    여러 시퀀스들의 곱집합
# itertools.permutations(p, r)	                    p 시퀀스의 요소 r개를 나열하는 순열
# itertools.combinations(p, r)	                    p 시퀀스의 요소 r개를 선택하는 조합
# itertools.combinations_with_replacement(p, r) 	p 시퀀스의 요소 r개를 중복을 허용해 선택하는 조합

# statistics 모듈은 산술평균, 표준편차 등 통계 계산에 자주 사용되는 함수를 모아놓은 모듈으로, 파이썬 버전 3.4 이상에서 사용할 수 있다.

# 함수	                        값 또는 기능
# statistics.median(seq)	    시퀀스의 중앙값
# statistics.mean(seq)	        시퀀스의 산술 평균
# statistics.harmonic_mean(seq)	시퀀스의 조화 평균
# statistics.stdev(seq)	        시퀀스의 표본 표준편차
# statistics.variance(seq)	    시퀀스의 표본 분산

