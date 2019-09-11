#-*- coding:utf-8 -*-
#Author:lhluo
import requests
import time
import pymysql
import json

print("登录")

def login():
	url='https://rpt.septnet.cn/Login/Post'
	s = {"_septnet_document":{"userCode":"13739247505","userPass":"123456","ruCode":"3408076"
	}}
	r=requests.post(url,data=s,verify=False)
	print(url)
	text=(r.text)
	print(text)
login()

print("获取科目原始满分和赋分满分结果")
def modifyuser():
  url='https://rpt.septnet.cn//ReportServer/getSourceAndFuFenFullScore'
  s = {
    "ExamGuid":"20190904-0310-11af-1b2b-71ba43585245"
  }
  cookie = {
    "yjticket": "0DFD4256C66F87AF4B7BE0D0AD752600_WEB_R2UMOVRQ5TOHZLIY",
    "RuCode":"3408076",
    "routers":"{%22title%22:%22%E6%95%B0%E6%8D%AE%E7%9C%8B%E6%9D%BF%22%2C%22path%22:%22/exhibition%22%2C%22query%22:{%22id%22:%2220190904-0310-11af-1b2b-71ba43585245%22%2C%22type%22:0%2C%22isnatural%22:0}}"
}
  r=requests.post(url,data=s,verify=False,cookies=cookie)
  print(url)
  text=(r.text)
  print(text)
  print (time.strftime("%H:%M:%S") + '\n')
modifyuser()

print("校验接口")
def queryPackage():
  url='http://115.28.115.220:7410/cmcc/userextension/queryPackage?usercode=19809778905'
  s = {
    "usercode":"19809778905"
  }
  r = requests.post(url, data=s,verify=False)
  text=(r.text)
  print(url)
  print(text)
  print (time.strftime("%H:%M:%S") + '\n')
queryPackage()  

def qhyd():
    url='http://111.44.229.249:7019/oppf'

print ("开发库查询用户是否存在")
def querymysql():
  conn = pymysql.connect(user='septnetyj',passwd='cc_55s77e44p7t',
                 host='dev.septnet.cn',db='ru',port=3990)
  cur = conn.cursor()
  cur.execute("SELECT * from ru_user where RU_User_code='19809778905'")
  for r in cur:           
    print (('\n'),"RU_User_code:"+str(r[0]),('\n'),"RU_User_type:"+str(r[3]),('\n'),"ru_user_createtime:"+str(r[8]),('\n'),"ru_user_id:"+str(r[9]))
  cur.close()    
  conn.close()
querymysql()
