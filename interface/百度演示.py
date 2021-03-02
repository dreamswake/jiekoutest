'''
    1.安装requests模块：模拟浏览器，jmeter发送http协议请求。
    2.



'''
import requests
#得到百度的所有返回数据
response = requests.get(url="http://www.baidu.com")

#先把response数据进行编码
response.encoding = "utf-8"
#提取数据
data = response.text

#打印出来，写到html页面里
f = open("百度.html","w+",encoding="utf-8")
f.write(data)
















