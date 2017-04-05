"""
Created on  Mar 5,  2016

:author: Shawn Li
:version: ff1

This file is for getting local time.
"""
import time

def get_local_time():

    local_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    return local_time


if __name__ == '__main__':
    LOCAL_TIME = get_local_time()
    print LOCAL_TIME
