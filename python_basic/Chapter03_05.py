# Chapter 03-05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '960523'}
b = {0: 'hello Python'}
c = {'arr' : [1,2,3,4]}
d = {
    'Name' : 'niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'a',
    'Status' : True
}
# 지나 친 FM
e = dict([
    ('Name', 'niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'a'),
    ('Status', True)
])
# 보통 이렇게 사용
f = dict(
    Name='niceman',
    City='seoul',
    Age=33,
    Grade='a',
    Status=True
)

print('a -', type(a), a)
print('a -', type(b), b)
print('a -', type(c), c)
print('a -', type(d), d)
print('a -', type(e), e)
print('a -', type(f), f)
print()

# 출력
print('a -', a['name']) # 없으면 키 에러가 발생
print('a -', a.get('name')) # 없으면 none이 출력 - 안전
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_key, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a- ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

# 무작위 pop
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'City' in d)

# 수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)

a.update(birth = '999999')
print('a - ', a)

temp = {'address' : 'Busan'}

a.update(temp)
print('a - ',a)


















