#coding:utf-8
import sys
import os
sys.path.append('..')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
reload(sys)
import config

def write_result(work_name, case_input, case_result, time_cal):
    path = config.workers_path + work_name + '_result.py'
    result = ["{\n"]

    str_0 = "'work_name':'" + work_name + "',"
    str_1 = "'case_input':'" + str(case_input) + "',"
    str_2 = "'case_result':'" + str(case_result) + "',"
    str_3 = "'time_cal':'" + str(time_cal) + "',"

    result.append(str_0)
    result.append(str_1)
    result.append(str_2)
    result.append(str_3)

    result.append("\n},")

    result_str = ''.join(result)
    with open(path, 'a') as f:
        f.write(result_str)

def write_to_csv(path='/Users/zengwei/test.csv'):
    from workers import create_result
    result = create_result.a
    print len(result)

    csv_list = []
    for node in result:
        for k,v in node.iteritems():
            csv_list.append(v)
            csv_list.append(',')
        csv_list.append('\n')
    csv_str = ''.join(csv_list)

    with open(path, 'w') as f:
        f.write(csv_str)



    pass
if __name__ == "__main__":

    write_to_csv()
    pass

