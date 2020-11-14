# 매핑

# 키 역할을 하는 데이터와 값 역할을 하는 데이터를 하나씩 짝지어 저장하는 데이터 구조다.

# 사전

menu_dict = {
    '아메리카노': 2500,
    '카페 라떼': 3000,
    '딸기 주스': 4000,
}

print('아메리카노' in menu_dict)
print('아이스 아메리카노' not in menu_dict)
print(menu_dict['딸기 주스'])
print(menu_dict.get('딸기 주스'))

menu_dict['에스프레소'] = 2000
print(menu_dict)

del menu_dict['딸기 주스']
print(menu_dict)

drink_list = ['아메리카노', '카페라떼', '에스프레소']
price_list = [2500, 3000, 1500]
menu_dict2 = dict(zip(drink_list, price_list))

print(menu_dict2)
print(menu_dict2.keys())
print(menu_dict2.values())
print(menu_dict2.items())

contact_list = []
contact_list.append({'name' : '강호동', 'phone' : '01011122211'})
contact_list.append({'name' : '이수근', 'phone' : '01012323351'})
print(contact_list[0])
print(contact_list[0]['phone'])
