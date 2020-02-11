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
e = dict([
    ('Name', 'niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'a'),
    ('Status', True)
])
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
print('a -', a.get('name')) # 없으면 none이 출력
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))