

#-*-coding:utf-8-*-
# author：linhan
import requests
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading
'''
def paper():
    f = open('log_file1.txt', 'a+')
    f.write("7net-test-paper" + '\n')
    headers = {"Content-Type": "application/x-www-form-urlencoded","version":"2.2.0"}
    s = {"userCode": "XXXXX", "password": 'zm123456'}
    url = 'https://szone-api.7net.cc/login'
    r = requests.post(url, data=s, headers=headers)
    text = (r.text)
    response = json.dumps(text)
    print (text)
    print (r.elapsed.total_seconds())
    f.write(response + '\n')
    f.write('\n')
    if (r.status_code==200) and eval(text)['message'] == 'success' :
        print ("结果正常")
        f.write('\n')
        f.write("Pass")
    else:
        print ("结果异常")
        f.write("Error")
        f.write('\n')
    f.write('=============================================================================' + '\n')
    f.write('=============================================================================' + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
'''
def getinfo():
    f = open('log_file1.txt', 'a+')
    f.write("7net-test-paper" + '\n')
    headers = {"Content-Type": "application/x-www-form-urlencoded","token":"XXXXXXXXXXXXXXXXXXXXXXXX","version":"2.2.0"}
    url = 'https://szone-api.7net.cc/UserInfo/GetUserInfo'
    r = requests.get(url,headers=headers)
    text = (r.text)
    response = json.dumps(text)
    print (text)
    print (r.elapsed.total_seconds())
    f.write(response + '\n')
    f.write('\n')
    if (r.status_code==200) and eval(text)['message'] == 'success' :
        print ("结果正常")
        f.write('\n')
        f.write("Pass")
    else:
        print ("结果异常")
        f.write("Error")
        f.write('\n')
    f.write('=============================================================================' + '\n')
    f.write('=============================================================================' + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

def thd():
    Threads = []
    for i in range(100):
        t=threading.Thread(target=getinfo)
        Threads.append(t)
    for t in Threads:
        t.start()
if __name__ == '__main__':
    thd()

'''
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,0);
while 1==1:
    time.sleep(second);
    paper()
sleeptime()
'''



