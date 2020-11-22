# 텍스트 양식화

# format() 메서드

physics, chemistry, biology = 80, 90, 70
form = '물리학: {}, 화학: {}, 생물학: {}'   # 양식 문자열 정의
form.format(physics, chemistry, biology)   # 양식 채워넣기
print(form)

print('물리학: {0}, 생물학: {2}, 화학: {1}'.format(50, 60, 70))
print('{0[0]}년 {0[1]}월 {0[2]}일'.format([2017, 11, 20]))

import math
print('원주율: {0.pi}'.format(math))

countries = [
    {'name': 'China', 'population': 1403500365},
    {'name': 'Japan', 'population': 126056362},
    {'name': 'South Korea', 'population': 51736224},
    {'name': 'Pitcairn Islands', 'population': 56},
]

# 공백 문자를 이용해 자리를 일정 길이만큼 채우도록 할 수 있다. {항목번호:자리길이}와 같은 형식을 사용하면 된다.
form = '나라: {0:16} | 인구: {1:10}'
for country in countries:
    print(form.format(country['name'], country['population']))
    
form = '나라: {0:>16} | 인구: {1:>10}'
for country in countries:
    print(form.format(country['name'], country['population']))
    

# 양식 문자열 리터럴
print(f'총점: {physics + chemistry + biology}')

# 양식 문자열 리터럴로 제곱 곱셈표 출력하기
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} ** {j} = {i ** j:10}')

# 텍스트 패턴

# 정규식 처리 메서드

# 함수	                        값 또는 기능
# re.compile(pattern)	        패턴 문자열 pattern을 패턴 객체로 컴파일한다
# re.search(pattern, string)	string에서 pattern과 매치하는 텍스트를 탐색한다 (임의 지점 매치)
# re.match(pattern, string)	    string에서 pattern과 매치하는 텍스트를 탐색한다 (시작점 매치)
# re.fullmatch(pattern, string)	string에서 pattern과 매치하는 텍스트를 탐색한다 (전체 매치)
# re.sub(pattern, repl, string)	string에서 pattern과 매치하는 텍스트를 repl로 치환한다
# re.split(pattern, string)	    string을 pattern을 기준으로 나눈다

import re                               # 정규식 모듈 임포트
pattern_string = r'파이썬'              # '파이썬' 패턴 문자열
pattern = re.compile(pattern_string)    # 패턴 문자열을 패턴 객체로 컴파일
print(re.search(pattern, '파이썬'))         # 매치한다: Match 객체 반환
print(re.search(pattern, '즐거운 파이썬'))  # 일부 텍스트와 매치한다

match = re.search('파이썬', '파이썬 프로그래밍')
if match:
    print('문자열에 패턴과 매치하는 텍스트가 존재함')
else:
    print('문자열에 패턴과 매치하는 텍스트가 존재하지 않음')
    
sample = '1789Python김파이fog'         # 샘플 텍스트
pattern = re.compile(r'[가-힣]{2,4}')  # 패턴
match = re.search(pattern, sample)     # 매치 결과를 match 변수에 대입
print(match.group())                   # 매치한 텍스트 구하기

sample = '이름: 김파이, 연락처: 010-1234-5678, 주소: 부산 어딘가'
pattern = re.compile(r'01\d-\d{3,4}-\d{4}')
match = re.search(pattern, sample)
print(match.group())

pattern = re.compile(r'[^가-힣]')
def hangeul_only(string):
    """
    한글만 남겨 반환하는 함수
    """
    match = re.sub(pattern, '', string)
    print(match)
    
hangeul_only('I like 파이썬 programming.')
hangeul_only('a1가b2나c3다d4라e5마f6바g7사')