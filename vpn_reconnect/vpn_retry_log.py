"""
Created on  Mar 19,  2016

:author: Shawn Li
:version: ff1

This file is logging error when reconnect VPN retry 3 time still failed.
"""
import os
from get_local_time import *
from vpn_check_config_parser import *

LOCAL_TIME = get_local_time()


def log_retry_error(failed_log_path, failed_log_name, failed_log_message):

    if not os.path.exists(failed_log_path):
        os.makedirs(failed_log_path)
    else:
        print "Retry failed log folder existed!"

    log_retry_failed_file = open(failed_log_path + LOCAL_TIME + failed_log_name, "w+")

    error_messages = [LOCAL_TIME + " " + failed_log_message + "\n"]

    log_retry_failed_file.writelines(error_messages)

    log_retry_failed_file.close()

    return True

if __name__ == '__main__':

    if log_retry_error(RETRY_FAILED_LOG_PATH, RETRY_FAILED_LOG_NAME, RETRY_FAILED_LOG_MESSAGE):
        print "retry failed log successfully!"
    else:
        print "retry failed log failed!"
