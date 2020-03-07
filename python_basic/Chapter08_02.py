# Chapter08-02
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제 1
import sys
print(sys.argv)

# 예제 2(강제 종료)
# sys.exit()

# 예제 3
print(sys.path)

# pickle : 객체 파일 읽기, 쓰기
import pickle

# 예제 4(쓰기)

f = open("test.obj", 'wb')
obj = {1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj, f)
f.close()

# 예제 5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()























