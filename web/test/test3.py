###************************************************************************
	# File Name: test3.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月05日 星期五 12时44分36秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
from bs4 import BeautifulSoup as BS
import urllib.parse


def get_url(url, url2, english):
    head = {}
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    data = {}
    data['from'] = 'en'
    data['to'] = 'zh'
    data['query'] = english
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    data['sign'] = '608144.894113'
    data['token'] = 'fcfaeb5d009ed1dca90074c0d64e689d'
    data['domain'] = 'common'
    data = urllib.parse.urlencode(data).encode('utf-8')
    lalr = urlreq.urlopen(url2, data)
    resp = urlreq.urlopen(url, data)
    '''
    req = urlreq.Request(url, data, head)
    res = urlreq.urlopen(req)
    '''
    http = resp.read().decode('utf-8')
    return http
'''
def get_img(http):
    soup = BS(http)
    scr = soup.body.
    
'''
if __name__ == '__main__':
    url2 = 'https://fanyi.baidu.com/langdetect'
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    english = input('输入英语单词: ')
    http = get_url(url, url2, english)
    print(http)
