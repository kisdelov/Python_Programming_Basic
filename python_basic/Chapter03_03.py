# Chapter03-03
# 파이썬 리스트
# 리스트 자료형(순서0, 중복0, 수정0, 삭제0)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foovar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print("c + d :", c + d)
print("c * 3 :", c * 3)
print("'test' + c[0]:", 'test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c)) # 변수 할당 시 같은 집 주소를 참조한다. 

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c'] #[['a', 'b', 'c']]
print('c -', c)
c[1] = ['a', 'b', 'c'] # 범위 지정 시, 그냥 원소로 들어가고, 단순 순번 지정 시, 리스트 안의 리스트가 들어가는 중첩이 됨
print('c -', c)
c[1:3] = []
print('c -', c)
del c[2] # 삭제
print('c -', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)
a.append(10) # 마지막 부분에 데이터 삽입
print('a -', a)
a.sort()
print('a -', a)
a.reverse()
print('a -', a)
print('a -', a.index(3), a[3])
a.insert(2, 7)
print('a -', a)
a.reverse()
print('a -', a)
# del a[-1]
# print('a -', a)
a.remove(10)
print('a -', a)
print('a -', a.pop()) # 끝에 있는 데이터를 꺼내오고 제거
print('a -', a)
print('a -', a.pop()) # 끝에 있는 데이터를 꺼내오고 제거
print('a -', a)
print('a -', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a -', a)

# 삭제 : remove(데이터), pop(끝 데이터), del(인덱스)

# 반복문 활용
while a:
    data = a.pop()
    print(data)




