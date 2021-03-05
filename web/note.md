---------------------------------------------------------------------------
	 File Name: note.md
	 Author: Fan Chongru
	 Mail: chongrufan123@gmail.com
	 Created Time: 2021年03月03日 星期三 14时30分17秒
   notes: 
 --------------------------------------------------------------------------

# web

<!-- vim-markdown-toc Marked -->

* [urllib包](#urllib包)
    * [request模块](#request模块)
    * [相应-请求](#相应-请求)
* [编码问题](#编码问题)
* [隐藏](#隐藏)
* [代理](#代理)
* [Beautiful Soup](#beautiful-soup)
* [正则表达式](#正则表达式)

<!-- vim-markdown-toc -->
## urllib包

### request模块
```
request.urlopen(url)    //读取url的数据
选项:
timeout:设置超连的时间, 单位是秒
html.decode("utf-8")    //解码, 将其他编码的字符串转换成Unicode格式
```
```
data是字典的格式
urllib.parse.urlencode(data).encode('utf-8')    将data数据编码为utf-8的格式
url = urllib.request.Request(url, date)
request.urlopen(url)    //以POST的形式访问URL
如果data是none, 那么请求就是GET方式
```

### 相应-请求
客户端发出请求, 服务端做出响应

## 编码问题
1.  中文输出乱码  
    获得此时的默认编码
    ```
    import sys
    sys.getdefaultencoding()
    ```
2.  Unicode
    Unicode码是统一各国文字的编码, 被称为万国码.他为每种语言设置了唯一的二进制编码表示形式  
    从Unicode到其他编码系统叫做编码, 从其他编码系统到Unicode是解码

## 隐藏
修改headers
1.  在Request时就加入head, 里面以字典形式存放要添加的内容
2.  在Request之后用req.add_header(key, value)来追加

## 代理
-   步骤
    1.  参数是一个字典{'类型' : '代理ip:端口号'}  
        proxy_support = urllib.request.ProxyHandler({})
    2.  定制, 创建一个opener  
        opener = urllib.request.build_opener(proxy_support)
    3.  安装opener  
        urllib.request.install_opener(opener)
    3.  调用opener  
        opener.open(url)

## Beautiful Soup
-   导入
    ```
    from bs4 import BeautifulSoup
    ```
-   传入数据  
    可以导入一个文件句柄, 也可以导入一段字符串, 默认自动选择解析器, 但也可以手动选择解析器
    ```
    BeautifulSoup(open("index.html"),
    ```
-   对象的种类
    BeautifulSoup将复杂的html文档转换为一个复杂的树形结构, 每个节点都是python对象, 所有对象可以归纳为4种
    -   Tag
        -   Name  
            每个tag都有自己的Name, 通过tag.name获取
            ```
            tag.name    获得tag的name
            ```
        -   Attributes  
            一个tag可能有多个属性, 可以被添加, 删除和修改, 操作方法和字典一样
            ```
            tag.attrs   字典形式返回属性
            tag['class']    返回属性的值
            ```
        -   多值属性  
            可以包含多个值的属性, 多值属性返回值是list
            ```
            css_soup.p['属性名']
            ```
    -   NevigableString  
        字符串常被包含在tag中, BS用NevigableString包装tag的字符串
        ```
        unicode(tag.string) 将NacigableString选项转变为unicode字符串
        ```
    -   BeautifulSoup  
        表示文档的全部内容
    -   comment  
        文档的注释部分, comment是一个特殊类型的NavigableString对象
-   遍历文档树
    -   子节点  
        一个tag包含的多个字符串和 其他的tag被称为这个tag的子节点
    -   tag的名字
        ```
        soup.head   获取tag的head
        soup.title  获取tag的title
        soup.body.b 获取body中第一个body
        soup.a      获取第一个以a开头的属性
        soup.find_all('a')  获取所有以a开头的属性
        tag.contents    将tag的子节点以列表形式列出
        for child in title_tag.children:
            print(child)    //对tag的子节点循环
        for child in head_tag.descendants:
            print(child)    //对tag的子孙节点进行递归循环
        title_tag.string    //如果tag只有一个子节点, 输出之, 如果有多个, 输出none
        for child in soup.strings:
            print(child)    //循环获取soup中的多个字符串
        ```
    -   父节点  
        每个tag或字符串都有父节点
        ```
        title_tag.parent    title的父节点
        for parent in link.parents:
            print(parent.name)  //遍历标签到根节点的所有节点
        ```

## 正则表达式
-   模块的导入
    ```
    import re
    ``` 
-   相关方法
    ```
    re.search(r匹配的字符, 目标字符串)  //匹配第一个目标字符串, 返回rematch类型
    re.findall(r匹配字符, 目标字符) //将所有目标字符放到一个列表中
    re.compile(r匹配对象)   //编译匹配对象, 之后search或findall就可以不用写匹配的字符了
    ```
    rematch类型相关的方法
    ```
    result.group    //匹配对应匹配的词组
    result.start    //匹配对应开始的范围
    result.end      //匹配对应结束的范围
    result.span     //匹配对应的范围
