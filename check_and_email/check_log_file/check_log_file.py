"""
Created on  Mar 6,  2016

:author: Shawn Li
:version: ff1

This file is for searching log files which have failed.
"""
# Search file in folder library
import os
import glob
# Get log file config parameters
from log_file_config_parser import LOG_FILE_LOCATION, LOG_FILE_FILTER
# import get_local_time method
from get_local_time import *

# Log parameters
LOCAL_TIME = get_local_time()
LOG_KEYWORD = LOCAL_TIME + '_Backups*.txt'
FAILURE_LOG_KEYWORD = LOG_FILE_FILTER

# Search log file to verify file is missing or not func
def search_missing_file(log_path, keyword):
    if glob.glob1(log_path, keyword):
        #print "Find %s log file" % keyword
        return True
    else:
        #print "%s log file is missing!" % keyword
        return False

# Search log file to verify file is failure or not func
def find_failure_log_files(file_path, keyword):
    file_list = os.listdir(file_path)
    file_filter = LOCAL_TIME + '_Backups-' + keyword + '.txt'
    if file_filter in file_list:
        #print "%s is a failure log file" % file_filter
        return True
    else:
        #print "%s_backup.txt isn't a failure log file" % LOCAL_TIME
        return False

# Mail func
if __name__ == '__main__':

    if search_missing_file(LOG_FILE_LOCATION, LOG_KEYWORD):
        if find_failure_log_files(LOG_FILE_LOCATION, FAILURE_LOG_KEYWORD):
            print "send log file is failure email!"
        else:
            print "Log file is existed and No failure today."

    else:
        print "send log file is missing email!"


