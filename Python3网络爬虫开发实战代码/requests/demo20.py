import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)  #避免验证错误后仍旧会给我们一个警告，这里采用忽略警告的方式