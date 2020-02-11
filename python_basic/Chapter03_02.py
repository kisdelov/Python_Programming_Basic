# Chapter03-02
# 파이썬 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = '' #""도 괜찮
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# I'm boy

print("I'm Boy")
print('I\'m Boy')
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 드라이브 경로 표시에 사용
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력 - 역슬래시를 사용
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2) 
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2) # 대소문자를 구분

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize :", str_o1.capitalize())
print("endswith? :", str_o2.endswith("e")) # 마지막 문자가 무엇인가
print("replace", str_o1.replace("thon", "Good"))
print("sorted: ", sorted(str_o1)) # 문자열을 기준에 맞게 정렬해서 리스트 형태로 반환
print("split: ", str_o4.split(' '))

print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('thon', ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("split: ", str_o4.split(' '))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스)
Im_str = "Good Boy!"

print(dir(Im_str)) # __iter__ 

# 출력
for i in Im_str:
    print(i)

# 슬라이싱 
str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3]) # 3-1까지 출력, 0 1 2
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_s1[:10]
print(str_sl[1:9:2]) # 세 번째 인수는 몇 개 단위로 점프하여 가져 올 것인가
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1]) # 역으로 출력

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로

