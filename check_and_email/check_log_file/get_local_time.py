"""
Created on  Mar 5,  2016

:author: Shawn Li
:version: ff1

This file is for getting local time.
"""
# Get local time library
import time

# Get local time func
def get_local_time():
    # change local time to xxxx-xx-xx format
    local_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return local_time

# Main func
if __name__ == '__main__':
    LOCAL_TIME = get_local_time()
    print LOCAL_TIME
