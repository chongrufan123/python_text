###************************************************************************
	# File Name: test4.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月05日 星期五 16时43分59秒
  # notes: 
###***********************************************************************
import requests

url = "https://fanyi.baidu.com/basetrans"
data = {"query": "你好，世界",
    "from": "zh",
    "to": "en"}
headers = {
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "referer": "https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma"}
response = requests.post(url,data = data,headers = headers)

print(response.content.decode())
