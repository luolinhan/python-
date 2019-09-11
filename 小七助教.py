#coding:utf-8

#auther:luolinhan

import json
import os
import sys
import time
import requests

f = open('log_file.txt','a+')
f.write ("七天教育-接口测试-小七助教"+'\n')
f.write ("执行时间："+time.strftime("%H:%M:%S")+'\n')
url ='http://115.28.113.150:7011/Stone.ExamService/StatisticsService/GetClassSubjectStatistics'

s = json.dumps({
"schoolGuid":"72cdec5c-1d28-4f08-bc35-e8c84c160b1c",
"classGuid":"485df4c5-0c83-470e-9e93-64b0a2003271",
"subject":"数学",
"examPlanGuids":"72deb0f8-233c-4bc4-bdda-cf5e89a22ebd",
"ExcellentRatio":"0.1",
"GoodRatio":"0.1",
"CommonRatio":"0.1",
"DifficultyRatio":"0.1",
"ExcellentCriticalAreaUp":"3",
"ExcellentCriticalAreaDown":"2",
"GoodCriticalAreaUp":"1",
"GoodCriticalAreaDown":"1"})
r = requests.post(url, data=s,verify=False)
text=json.loads(r.text)

f.write(url+'\n')
f.write('返回结果'+'\n')
print(text)

f.write('=====================分割线======================'+'\n')


f.flush()
f.close()
