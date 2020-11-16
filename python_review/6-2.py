# 반복

# while 문 : 지정 조건이 유지되는 동안 코드 반복

i = 0

while i < 3:
    print('안녕')
    i += 1

# 컬렉션 순회

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
index = 0

while index < len(rainbow):
    print(rainbow[index])
    index += 1

# 흐름이 예정되지 않은 반복

# text = "아무 메시지나 입력하세요. 그만하려면 '그만'을 입력하세요."
# while text != '그만':
#     print('컴퓨터 : ' + text)
#     text = input()

# 무한 반복

# while True :
#     print('이 메시지는 무한히 반복 출력됩니다.')

# for 문

for color in rainbow:
    print(color)

def my_sum(numbers):
    """
    numbers의 모든 요소의 합을 반환한다.
    """
    total = 0
    for n in numbers:
        total += n
    return total

print(my_sum([1, 2, 3, 4, 5]))

# 문제 1

# n = 100
# while n < 10000 :
#     total = 0
#     total += n
#     n += 5
# print (total)

# # 문제 2

# for n in range(100,10000,5):
#     total2 = 0
#     total2 += n

# print(total2)

# 문제 3

def my_max(numbers2):
    for n in numbers2:
        max = 0
        if max > n:
            continue
        max = n
    return max

print(my_max([1,2,3,4,5,6,7,8]))

# 문제 4

def is_prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
            break
    else:
        return True

total = 0
for k in range(1,100):
    if is_prime(k):
        total += k

print(total)


