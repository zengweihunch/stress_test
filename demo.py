#coding:utf-8

import multiprocessing
from multiprocessing import Pool

import os
import config
import time

from data import weixin, toutiao
from utils import result

def get_worker_path(worker_name):
    return config.workers_path + worker_name + '.py '


def run_one_work(pid, worker_name, param):
    print '>>>>>:', param
    cmd = 'python ' + get_worker_path(worker_name) + ' ' + "'" + param + "'"
    print 'cmd: ', cmd
    os.system(cmd)


def run(worker_num, work_name, data, pool_size=8, off_set=80):
    start = time.time()
    pool = Pool(processes=pool_size)    # set the processes max number worker_num

    for i in range(off_set, off_set + worker_num):
        result = pool.apply_async(run_one_work, (i, work_name, data[i], ))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'

    end = time.time()
    print '>>>>time', end-start


def case1():
    work_name = 'create'
    work_result_path = config.workers_path + work_name + '_result.py'
    print '<<<<<<work'
    with open(work_result_path, 'w') as f:
        f.write('#coding:utf-8\n')
        f.write('a=[\n')

    for i in range(80, 180):

        run_one_work(i, work_name, weixin.weixin_doc_url[i])

    with open(work_result_path, 'a') as f:
        f.write('\n]')
    print '<<<<<<write_to_csv'
    #result.write_to_csv()
    pass

if __name__ == "__main__":
    #run(10)
    # 1
    #case1()

    ## 2 压力测试，数据源，微信
    #work_name = 'create'
    #work_result_path = config.workers_path + work_name + '_result.py'
    #print '<<<<<<work'
    #run(100, work_name, weixin.weixin_doc_url)
    ##result.write_to_csv()

    # 3 压力测试，数据源，今日头条
    work_name = 'create'
    data_origin = 'toutiao'
    print 'end'
    run(100, work_name, toutiao.toutiao_url, pool_size=1, off_set=30)
