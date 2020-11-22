# 텍스트 파일 읽고 쓰기

# open() 함수로 파일을 열어, 파일 객체를 얻는다.
# 파일 객체에서 입력 또는 출력을 수행한다.
# 파일 객체의 close() 메서드로 파일을 닫는다.

# print('당신의 이름은 무엇인가요?')
# name = input()

# with open('python_review/hello.txt', 'w') as file:
#     print(name, '님 반가워요.', file=file)

# file = open('python_review/years.txt')  # 텍스트 파일 열기
# for line in file:         # 파일 내용을 한 행씩 읽어 화면에 출력
#     print(line)
# file.close()              # 파일 닫기

# with open('python_review/years.txt') as file:  # 텍스트 파일 열기
#     for line in file:            # 파일 내용을 한 행씩 읽어 화면에 출력
#         print(line)
        
# from datetime import date
# today = date.today()
# text = f'안녕하세요! 오늘은 {today.month}월 {today.day}일 입니다.\n'

# with open('python_review/hello.txt', 'a') as file:
#     file.write(text)
    
# try:
#     with open('python_review/한번만_기록.txt', 'x') as file:
#         file.write('이 파일은 한 번만 작성됩니다.')
# except FileExistsError:
#     print('파일이 이미 존재합니다.')
    
# 열기 모드	    의미
# r	            읽기(read) 모드 (기본값이며 생략 가능)
# w	            쓰기(write) 모드
# a	            덧붙이기(append) 모드
# x	            배타적(exclusive) 쓰기 모드
# t	            텍스트(text) 모드 (기본값이며 생략 가능)
# b	            이진(binary) 모드

# with open('python_review/time.txt', 'r') as file:
#     data = file.read()

# print(data)   # 읽어들인 내용을 확인해보자

# file = open('python_review/time.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# with open('python_review/time.txt') as file:
#     for line in file:
#         print(line, end='')

# def cp(src, dst):
#     with open(src, 'r') as file1:
#         data1 = file1.read()
#         with open(dst, 'w') as file2:
#             print(data1, file=file2)
#             file2.write(data1)
            
# cp('original.txt', 'clone.txt')


# 데이터 직렬화하기

# 약속에 따라 입체적인 데이터를 텍스트나 바이트로 표현하는 것을 직렬화(serialization)라고 한다.

# CSV: 표 형식의 정보 나타내기
# CSV(comma-separated values, 쉼표로 구분된 값)는 표(table) 형식

import csv  # csv 모듈 임포트
import pprint

# movies.csv 파일 열기
with open('python_review/movies.csv') as file:
    reader = csv.reader(file)  # CSV 파일을 읽어들이는 읽기 객체
    movies = list(reader)      # CSV 파일 내용을 리스트로 읽어들인다

pprint.pprint(movies)  # 읽어들인 내용을 화면에 출력

table = [
    ['title', 'genre', 'year'],
    ['Interstella', 'SF', '2014'],
    ['Braveheart', 'Drama', '1995'],
    ['Mary Poppins', 'Fantasy', '1964'],
    ['Gloomy Sunday', 'Drama', '2000'],
]

# movies_output.csv 파일을 쓰기 모드로 열기
with open('python_review/movies_output.csv', 'w') as file:
    writer = csv.writer(file)  # CSV 파일을 작성하는 쓰기 객체
    writer.writerows(table)    # 표를 전체 행을 CSV 파일에 써넣는다
    
# JSON: 입체적인 데이터 나타내기

# 숫자와 따옴표 데이터는 각각 파이썬의 수와 문자열에 대응된다.
# 중괄호 표현(객체)은 파이썬의 사전에 대응된다.
# 대괄호 표현(배열)은 파이썬의 리스트에 대응된다.
# 작은따옴표가 아니라 큰따옴표를 사용한다.
# 중괄호와 대괄호 안의 마지막 데이터 뒤에 콤마를 붙여서는 안 된다.
# 줄바꿈과 들여쓰기 등 공백 문자는 생략될 수 있다.

import json   # json 모듈 임포트

# 직렬화하려는 데이터
data = [
    {
        'title': 'Interstella',
        'genre': 'SF',
        'year': 2014,
        'starring': ['M. McConaughey', 'A. Hathaway', 'J. Chastain'],
    },
    {
        'title': 'Mary Poppins',
        'genre': 'Fantasy',
        'year': 1964,
        'starring': ['J. Andrews', 'D. Van Dyke'],
    },
]

json_data = json.dumps(data)  # 컬렉션을 JSON으로 직렬화
print(json_data)              # 직렬화된 텍스트 확인
with open('python_review/movies.json', 'w') as file:  # 파일로 저장
    file.write(json_data)
    
with open('python_review/movies.json') as file:  # 텍스트 파일을 읽어들인다
    json_data = file.read()

data = json.loads(json_data)  # 읽어들인 텍스트 데이터를 역직렬화
pprint.pprint(data)  # 해석된 데이터 확인

# 연습 문제

with open('python_review/countries.csv') as file:
    reader = csv.reader(file)  # CSV 파일을 읽어들이는 읽기 객체
    countries = list(reader)      # CSV 파일 내용을 리스트로 읽어들인다

countries[0].append('density')
for i in range(1, len(countries)):
    countries[i].append(round(int(countries[i][1])/int(countries[i][2])))

pprint.pprint(countries)  # 읽어들인 내용을 화면에 출력

big_countries = sorted(countries[1:], key=lambda country: country[3], reverse=True)

pprint.pprint(big_countries)

print()
print('인구밀도 순 나라')
for i in range(1, len(countries)):
        print('나라: {:15} 인구밀도 : {:7}'.format(countries[i][0], countries[i][3]))
        
        
# 파일 시스템에서 작업하기
# .: 현재 디렉터리
# ..: 한 단계 위의 디렉터리
# C:\: (윈도우) 첫번째 하드 디스크
# C:\Users\bakyeono\Documents\: (윈도우) 사용자 문서 디렉터리
# /: (유닉스) 파일 시스템의 루트
# /home/bakyeono: (유닉스) 사용자 디렉터리

from pathlib import Path   # pathlib 모듈에서 Path 클래스 임포트
print(Path('.'))     # 현재 디렉터리의 경로
print(Path('C:/'))   # 하드 디스크의 경로

# 속성 또는 메서드	    값 또는 기능
# exists()	        대상이 존재하는지 검사한다
# is_file()	        대상이 파일인지 검사한다
# is_dir()	        대상이 디렉터리인지 검사한다
# parent	        한 단계 위의 경로
# name	            대상의 이름
# suffix	        대상의 확장자
# with_name(new)	이름을 new로 변경한 경로를 반환한다
# with_suffix(new)	확장자를 new로 변경한 경로를 반환한다
# iterdir()	        대상 디렉터리를 순회하는 반복자를 반환한다
# mkdir()	(주의)  대상 디렉터리를 생성한다
# touch()	(주의)  빈 파일을 생성한다
# replace(new)	(주의) 대상의 경로를 new로 바꾼다
# rmdir()	(주의)  대상 디렉터리를 삭제한다
# unlink()	(주의)  대상 파일을 삭제한다

path = Path('F:\Python_Programming_Basic\python_review')
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.parent)
print(path.name)
print(path.suffix)

def ls(path):
    """path 디렉터리에 포함된 모든 하위 항목을 화면에 출력한다."""
    path_obj = Path(path)            # 전달된 경로의 Path 객체 생성
    
    for item in path_obj.iterdir():  # 모든 하위 항목을 순회하며
        print(item)                  # 화면에 출력

ls('F:\Python_Programming_Basic\python_review')  # C:\ 경로의 모든 하위 항목 출력