# Chapter09_01
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, t - 텍스트, b - 바이너리
# 상대 경로('../, ./'), 절대 경로('C:\a\b\c..')

# 파일 읽기(Read)
# 예제 1

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)

cts = f.read()
print(cts)

# 반드시 close
f.close()





