# -*- coding: utf-8 -*
import json
import requests
from requests.exceptions import RequestException
import re
import time
import io


#抓取首页
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS 10_13_3)AppleWEBkIT/537.36 (KHTML,like Gecko)Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#正则提取
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

#写入文本文件
def write_to_file(content):
    with io.open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n') 
        #通过JSON库的dumps()方法实现字典的序列化，并指定ensure_ascii参数为FALSE，这样可以保证输出结果是中文形式而不是Unicode编码

#因为是分页爬取，所以加入一个遍历，引入offset参数，并定义main()函数调用上面的函数
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':    #这一行代码的作用表示当在导入这个spider.py这个文件时，该代码下的代码将不被运行
#当.py文件被当做一个模块导入时，我们不希望某部分代码被运行时就可以使用if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)  #延时等待
