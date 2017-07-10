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
    cmd_str = "curl " + url + " -H 'Origin: http://test.zenvideo.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://test.zenvideo.cn/' -H 'Cookie: csrftoken=yrbApRVUyxUHSa3hBDvja5x6256rioyDSqipXPUoOMJtIndar4sfmVr1BxmKsXJS; sessionid=v9laofa1maabrfjzbj21uvrnkbdfaetj; cn_1262676077_dplus=%7B%22distinct_id%22%3A%20%2215cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201499442086%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201499442086%7D%2C%22initial_view_time%22%3A%20%221499440285%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; __insp_wid=2074501620; __insp_nv=false; __insp_targlpu=aHR0cDovL3Rlc3QuemVudmlkZW8uY24vIy9ob21l; __insp_targlpt=5pm65b2xLeeUqOinhumikeiusui%2FsOS9oOeahOaVheS6iw%3D%3D; CNZZDATA1262334663=761505194-1498216293-%7C1499648567; __insp_sid=2059194667; __insp_uid=2350901931; __insp_slim=1499657717908; cn_1262334663_dplus=%7B%22distinct_id%22%3A%20%2215cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d%22%2C%22initial_view_time%22%3A%20%221498982338%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22sp%22%3A%20%7B%22phoneNum%22%3A%20%2215057136454%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201499586335%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201499586335%7D%7D; UM_distinctid=15cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d' -H 'Connection: keep-alive' --data 'input_text=" + code_url(input_txt) + "' --compressed"

    '''
    "curl " ＋ url + " -H 'Origin: http://test.zenvideo.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://test.zenvideo.cn/' -H 'Cookie: csrftoken=yrbApRVUyxUHSa3hBDvja5x6256rioyDSqipXPUoOMJtIndar4sfmVr1BxmKsXJS; sessionid=v9laofa1maabrfjzbj21uvrnkbdfaetj; cn_1262676077_dplus=%7B%22distinct_id%22%3A%20%2215cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201499442086%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201499442086%7D%2C%22initial_view_time%22%3A%20%221499440285%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; __insp_wid=2074501620; __insp_nv=false; __insp_targlpu=aHR0cDovL3Rlc3QuemVudmlkZW8uY24vIy9ob21l; __insp_targlpt=5pm65b2xLeeUqOinhumikeiusui%2FsOS9oOeahOaVheS6iw%3D%3D; CNZZDATA1262334663=761505194-1498216293-%7C1499648567; __insp_sid=2059194667; __insp_uid=2350901931; __insp_slim=1499657717908; cn_1262334663_dplus=%7B%22distinct_id%22%3A%20%2215cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d%22%2C%22initial_view_time%22%3A%20%221498982338%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22sp%22%3A%20%7B%22phoneNum%22%3A%20%2215057136454%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201499586335%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201499586335%7D%7D; UM_distinctid=15cd4bbd3b40-06fa77c8ae37e-3063750b-384000-15cd4bbd3b559d' -H 'Connection: keep-alive' --data 'input_text=" + code_url(input_txt) + "' --compressed
    '''
    return cmd_str


def test():
    url = weixin.weixin_doc_url[0]
    print code_url(url)

def create(input_txt):
    url = 'http://test.zenvideo.cn/project/v2/create/'
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
