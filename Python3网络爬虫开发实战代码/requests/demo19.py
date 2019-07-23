import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)
#上面这里的返回结果是SSLError， 表示验证证书错误

response = requests.get('https://www.12306.cn', verify=False)   #通过verify避免验证错误
print(response.status_code)
