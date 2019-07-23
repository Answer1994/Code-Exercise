import requests

r = requests.get('https://www.taobao.com', timeout=1)  #超时设置
print(r.status_code)