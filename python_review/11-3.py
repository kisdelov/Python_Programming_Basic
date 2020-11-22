# 운영 체제의 시간 관련 기능

# time 모듈은 운영 체제가 제공하는 다양한 시간 기능을 다루는 모듈이다. 운영 체제마다 시간을 다루는 방식이 다르기 때문에 이 모듈의 함수들은 어떤 운영 체제에서 실행하느냐에 따라 결과가 다르다.

import time
print(time.time())

print(time.time())

now = time.gmtime(time.time())
print(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

# 날짜와 시각

# time 모듈이 제공하는 기능은 복잡한 시간 개념을 다루기에는 너무 단순하다. datetime 모듈은 시간을 날짜와 시각으로 표현하는 방법을 제공해, 시간을 좀더 인간의 관점에 가깝게 다루도록 해준다.

from datetime import date
print(date(1789, 7, 14))
print(date(year=1986, month=3, day=6))
print(date.today())

# 속성 또는 메서드	    값 또는 기능
# year	                년
# month	                월
# day	                일
# weekday()	            요일 (월요일=0, 일요일=6)
# isoformat()	        ISO 표준 문자열 표현
# strftime(format)	    문자열 표현

from datetime import time

print(time(15))
print(time(hour=15, minute=30, second=45, microsecond=200000))

# 속성 또는 메서드	    값 또는 기능
# hour	                시
# minute	            분
# second	            초
# microsecond	        마이크로초
# isoformat()	        ISO 표준 문자열 표현
# strftime(format)	    문자열 표현

from datetime import datetime
print(datetime(2017, 11, 14, 8, 30, 50, 200000))
print(datetime.now())
now = datetime.now()

print(now.year, now.month, now.day, '월화수목금토일'[now.weekday()])
print(now.hour, now.minute, now.second, now.microsecond)
print(now.date(), now.time())
print(now.isoformat())


# 기호	의미	            출력 예(2001-02-03 04:05:06 기준)
# %Y	년 (네 자리)	    2001
# %y	년 (두 자리)	    01
# %m	월 (두 자리)	    02
# %d	일 (두 자리)	    03
# %A	요일	            Saturday
# %H	시 (24시간)	        04
# %I	시 (12시간)	        04
# %p	오전, 오후	        AM
# %M	분 (두 자리)	    05
# %S	초 (두 자리)	    06
# %f	마이크로초	        000000
# %%	% 기호	            %

mayday = date(2017, 5, 1)
morning = time(8, 30)
now = datetime.now()
print(str(mayday))
print(str(morning))
print(str(now))
print(mayday.strftime('%Y/%m/%d'))
print(morning.strftime('%H:%M'))
print(now.strftime('%m월 %d일 %H시 %M분'))

from datetime import timedelta
print(timedelta(weeks=3, days=5))
print(timedelta(days=2, hours=3, minutes=30))

now = datetime.now()
after_1000h = timedelta(hours=1000)
print(now + after_1000h)

birthday = date(1996, 5, 23)
print(date.today() - birthday)

def counting_age(birth_date):
    birth_year = birth_date.year
    now_year = date.today()
    return now_year.year - birth_year + 1

print(counting_age(birthday))

def full_age(birth_date):
    birth = birth_date
    today = date.today()

    if (today.month > birth.month) or ((today.month == birth.month) and (today.day>birth.day)):
        return today.year - birth.year

    else:
        return today.year - birth.year - 1

print(full_age(birthday))
