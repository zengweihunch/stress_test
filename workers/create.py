#coding:utf-8
import sys
import os
sys.path.append('..')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

reload(sys)
from utils import cmd_utils
from data import weixin
import urllib
from utils import result
import time

def code_url(url):
    url_code = urllib.quote(url)
    return url_code


def get_curl_cmd(url, input_txt):
    cmd_str = " curl '" + url + "' -H 'Origin: http://120.55.17.36' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://120.55.17.36/static/index.html' -H 'Cookie: __insp_wid=2074501620; __insp_nv=true; __insp_targlpu=aHR0cDovLzEyMC41NS4xNy4zNi9zdGF0aWMvaW5kZXguaHRtbA%3D%3D; __insp_targlpt=5pm65b2xLeeUqOinhumikeiusui%2FsOS9oOeahOaVheS6iw%3D%3D; csrftoken=pBI72pI51Mbewl02TMN864aAIzhnxpzeI1l75kJqYO2pxfgDCNiPmVuhUdGJgGKN; sessionid=w4vmf7jd7txhaisy3a30rdjhl4192pt5; __insp_sid=1848324935; __insp_uid=2306697600; __insp_slim=1497524221405' -H 'Proxy-Connection: keep-alive' --data 'input_text=" + code_url(
        input_txt) + "' --compressed"
    return cmd_str
    pass


def test():
    url = weixin.weixin_doc_url[0]
    print code_url(url)

def create(input_txt):
    url = 'http://120.55.17.36/project/create/'
    #input_txt = weixin.weixin_doc_url[0]
    cmd_str = get_curl_cmd(url, input_txt)
    a = time.time()
    try:
        result_cmd = cmd_utils.run_sys_command(cmd_str)
    except Exception as e:
        result_cmd = e.message
        print ">>>>>>>>>>>>e.message:", e.message
    b = time.time()
    time_cal = str(b-a)

    success_flag = '"message": "ok", "code": 0'
    assets_failed_flag = '"assets": {}'
    timeline_failed_flag = '"timeline": []'
    if assets_failed_flag in str(result_cmd):
        case_result = 2
    elif success_flag in str(result_cmd):
        case_result = 1
    elif timeline_failed_flag in str(result_cmd):
        case_result = 3
    else:
        case_result = 0 #false
    print '>>>>>>result:', case_result
    result.write_result('create', input_txt, case_result, time_cal)

if __name__ == '__main__':
    url = 'http://mp.weixin.qq.com/s?__biz=MzIwMzAzNDk2OA==&mid=2651603088&idx=7&sn=083e7217e2eb27c15d67b1ae888ff011&scene=0'

    print 'parm1:', sys.argv[1]
    url = sys.argv[1]
    create(url)

    #print test()
