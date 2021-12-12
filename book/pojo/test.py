import time
import urllib3,requests
from functools import wraps

def get_time(api):
    """
    获取时间
    :param api:
    :return:
    """
    print("现在运行get_time(api)")
    @wraps(api)
    def get():
        print("现在运行get()")
        start = time.time();
        api()
        stop = time.time();
        print("函数运行时间为",stop-start)
    return get

@get_time
def get_api():
    """
    获取接口信息
    :return:
    """
    print("现在运行get_api()")
    url = "https://easy-mock.home.qyzhg.com:10443/mock/61922bfd6e616600201c7c3e/test/getapi"
    json = {}
    urllib3.disable_warnings()
    time.sleep(3)
    result = requests.post(url, json=json, verify=False).json()
    print(result)

    if __name__ == '__main__':
        get_api()
        # 打印函数里注释的内容
        print(get_time.__doc__)
        # 打印get_time这个函数的函数名
        print(get_time.__name__)
        # 打印get_api这个函数里的注释内容
        print(get_api.__doc__)
