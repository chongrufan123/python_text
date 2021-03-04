###************************************************************************
	# File Name: code1_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月04日 星期四 12时03分17秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
import easygui as g

while 1:
    fieldNames = ["长", "宽"]
    title = '下载一直瞄'
    msg = '请填写瞄的尺寸'
    fieldvalue = []
    fieldvalue = g.multenterbox(msg, title, fieldNames)
    for each in range(2):
        try:
            aa = int(fieldvalue[each])
        except ValueError:
            fieldvalue[each] = 600 if each else 400

    url = "http://placekitten.com/g/" + str(fieldvalue[1]) + "/" + str(fieldvalue[0])
    cat_image = urlreq.urlopen(url).read()

    msg2 = '请输入下载的文件名称'
    filename = g.enterbox(msg2, title)
    filename = filename + '.jpg'

    with open(filename, 'wb') as f:
        f.write(cat_image)
    if g.ccbox("下载完成, 还要继续下载吗", choices=("继续", "不了")):
        pass
    else:
        break
        


