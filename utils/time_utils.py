# coding:utf-8
import time


def exeTime(func):
    def newfunc(*args, **args2):
        t0 = time.time()
        back = func(*args, **args2)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
        return back
    return newfunc
