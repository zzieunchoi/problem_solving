# python date 변환하기

## date to string

```python
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")

print(date_time)
# '2021년 12월 31일 13시 35분 42.657813초'
```



## string to date

```python
from datetime import datetime
date_time_str = '2021-06-27 06:51:22'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
print(date_time_obj)
# 2021-06-27 06:51:22
```



## date 날짜 더하기

```python
import datetime

now = datetime.now()
now_after_777 = now + datetime.timedelta(days = 777)
print(now_after_777) 
# 2021-04-14 21:15:54.891525

# seconds, microseconds, milliseconds, minutes, hours, weeks
```

