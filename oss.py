import os, gevent, random, time
import oss2

#配置连接oss时需要的各项参数和参数值
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAILJYSLecZwjz0')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'JLhC6UDzvsn5AI07ASFNO1gpeEyFgc')
bucket_name = os.getenv('OSS_TEST_BUCKET', '7netapplet-beijing')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')

# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

# OSS官方提供的上传文件接口（目标路径及文件名，本地路径及文件名）
# bucket.put_object_from_file('test/20190903/db_qitianxuetang/iOS/555.txt', r'D:\testdata\555.txt')


def task1(i):

    gevent.sleep(random.randint(0, 2) * 0.001)
    t=str(time.time())
    bucket.put_object_from_file('test/20190903/db_qitianxuetang/iOS/'+t+'.txt', r'D:\testdata\555.txt')

def asynchronous():
    start = time.process_time()
    gev_list1 = [gevent.spawn(task1, i) for i in range(5)]

    gevent.joinall(gev_list1)
    elapsed = (time.process_time() - start)
    print("Time used:", elapsed)


print("asynchronous:")
asynchronous()
