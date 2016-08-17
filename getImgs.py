#coding=utf-8
import urllib.request
import re

def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    req=urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    html = html.decode('utf8')
    return html

def getImg(html):
    reg=r'src="(.+?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'E:\pythonImgs\%s.jpg'%x)
        x+=1
    print (imglist)

html = getHtml("http://www.tooopen.com/view/927495.html")
getImg(html)
