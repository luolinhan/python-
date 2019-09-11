__author__ = 'zhouao'


from locust import HttpLocust,TaskSet,task
import queue
from queue import Queue
from random import randint


class test_taskset(TaskSet):
    @task


    def on_start(self):
        self.login()

    def login_user(self):
        filename=r"/Users/lhluo/Desktop/github/python-/codeandpass.txt"
        fr = open(filename,'r+')
        infile_content = fr.read().splitlines()
        list_temp1 = []
        for each in infile_content:
            #list_temp = []
            list_temp=each.split()
            data1 = {
                "Code":str(list_temp[0]),
                "Pass":str(list_temp[1]),
            }
            list_temp1.append(data1)
        number =randint(1, 7)
        data=list_temp1[number]
        print(data)
        return data

    def login(self):
        data =self.login_user()
        print(data)

        print('actually user and password is {} and {}'.format(data['Code'], data['Pass']))
        #payload = {
        #    'Code': data['Code'],
        #    'Pass': data['Pass'],
        #}
        self.client.post('/Login', data)

class test_run(HttpLocust):
    host = 'http://office.dev2.septnet.cn'
    task_set = test_taskset
    #user_data = queue.Queue()
    min_wait=2000
    max_wait = 5000




