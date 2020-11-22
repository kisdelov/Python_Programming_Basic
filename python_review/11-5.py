# 웹 커뮤니케이션

# 웹에 정보 요청하기

import urllib.request

def request(url):
    """지정한 url의 웹 문서를 요청하여, 본문을 반환한다."""
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('utf-8')
    return text_data

import pprint
import json
print(request('https://python.bakyeono.net/chapter-11-5.html'))
movies = json.loads(request('https://python.bakyeono.net/data/movies.json'))
print(movies)
sorted_by_year = sorted(movies, key = lambda movie: movie['year'])

for movie in sorted_by_year:
    print(str(movie['year']) + ' ' + movie['title'].upper())
    
# URL은 인터넷 공간에 존재하는 자원을 가리키기 위한 절대 주소다. URL을 작성하는 양식은 다음과 같이 정해져 있다.
# 프로토콜://계정:패스워드@호스트:포트번호/하위경로?질의조건    #색인

url = 'https://python.bakyeono.net/data/movies.json'
url_parts = urllib.parse.urlsplit(url)
print(url_parts[0])
print(url_parts[1])   # 호스트 확인
print(url_parts[2])   # 하위 경로 확인

url_parts = list(url_parts)
url_parts[2] = '/chapter-11.html'
print(urllib.parse.urlunsplit(url_parts))

# 퍼센트 인코딩(한글이 들어간 문서)
base_url = 'https://ko.wikipedia.org'
path = urllib.parse.quote('/wiki/파이썬')
url = base_url + path
# print(urllib.request.urlopen(url).read().decode('utf-8'))

