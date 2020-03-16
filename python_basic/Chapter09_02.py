# Chapter09-02
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제 1
with open('./python_basic/resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # Header Skip
    # 객체 확인
    print(reader)

    # 타입 확인
    print(type(reader))

    # 속성 확인
    print(dir(reader)) # __iter__
    print()

    for c in reader:
        # print(c)
        # 타입 확인(리스트)
        # print(type(c))
        # list to str
        print(' : '.join(c))

# 예제 2
with open('./python_basic/resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

# 예제 3
with open('./python_basic/resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # __iter__
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('---------------')









