import requests
import time

def check_res_status(url):
    """
    サービスにリクエストを送信し正常性のチェックを行う
    200:   Service is ok
    200以外：Service is abnormal
    """
    res = requests.get(url)
    if res.status_code == 200:
        print('Service is ok')
    else:
        print('Service is abnormal')

def main():
    # 秒に一度サービスの正常性監視を行う
    while(True):
        check_res_status('https://ushizawa-portfolio.com')
        time.sleep(3)


if __name__ == '__main__':
    main()

