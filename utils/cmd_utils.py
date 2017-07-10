import os
import subprocess

import logging

logger = logging.getLogger(__name__)


def run_sys_command(cmd_arr, extra_env=None):

    def need_to_run_shell():
        for cmd_seg in cmd_arr:
            if '"' in cmd_seg:
                return True
        return False

    if type(cmd_arr) == str:
        cmd_str = cmd_arr
        pass
    elif type(cmd_arr) == list:
        cmd_str = ' '.join(cmd_arr)
    else:
        raise Exception('CHECK CMD TYPE!')

    logger.info('Running command: %s' % cmd_str)
    #print cmd_str

    my_env = os.environ.copy()
    #print 'my_env:', my_env
    if extra_env is not None:
        my_env.update(extra_env)

    #if need_to_run_shell():
    #    proc = subprocess.Popen(cmd_str, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env, shell=True)
    #else:
    proc = subprocess.Popen(cmd_str, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env, shell=True)

    ret = proc.communicate()

    if proc.returncode != 0:
        raise Exception('Running command %s with non-zero return code:\nSTDOUT: %s\nSTDERR: %s' % (cmd_str, ret[0], ret[1]))

    print '>>>>>>>type',type(ret)
    return ret

if __name__ == "__main__":
    from cmd_utils import run_sys_command
    print 'start...'
    cmd = ['/mnt/tmp/tts_snippet']

    cmd.append('-N')
    cmd.append(str('13307_6_1_None_None'))
    text = ''
    cmd.append(text.encode('utf-8'))

    run_sys_command(cmd, {'LD_LIBRARY_PATH': '/mnt/tmp'})
