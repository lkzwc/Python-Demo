import os
import requests
import time

requests =requests.Session()

headers={
    'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
    'Referer':'http://membernew.yundasys.com:15116/member.website/hywz/login.html',
 }


def getImage():
    response = requests.get('http://membernew.yundasys.com:15116/ydaccount/getImageCode',params={"dataStr":time.time()*1000,"headers":headers})
    with open("a.jpg","wb") as file:
        file.write(response.content)

def login():
    headers2={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Content-Length':'275',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'membernew.yundasys.com:15116',
        'Origin': 'http://membernew.yundasys.com:15116',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
        'Referer':'http://membernew.yundasys.com:15116/member.website/hywz/login.html',
        'X-Requested-With':'XMLHttpRequest'
    }

    data={
        'action':'member.account_new.login_new_check_code',
        'version':'V1.0',
        'req_time':str(int(time.time()*1000)),
        'appid':'ydmb',
        'data':{"loginName":"15555221545","password":"e21ac30447efe9c626a14184a662495d","validCode":input("输入验证码"),"sessionid":str(time.time()*1000)}
    }
    res =requests.post('http://membernew.yundasys.com:15116/opserver/ydmb/interface.do?member.account_new.login_new_check_code&ydmb',data=data,headers=headers2)
    res.encoding = 'UTF-8'
    print(res.text)
    print(type(res.cookies), res.cookies)

def getInfo():
    data={
        'action': 'member.order.orderList',
        'req_time': int(time.time()*1000),
        'version': 'V1.0',
        'appid': 'ydmb',
        'openid': requests.cookies,
        'data': {"type":"S","currentPage":"1","pageSize":"10","condition":"","orderStatus":"","startDate":"","endDate":""}
    }
    
    res = requests.post('http://membernew.yundasys.com:15116/opserver/ydmb/interface.do',data=data)
    print(res.text)

getImage()
print("1111111")
login()
getInfo()
