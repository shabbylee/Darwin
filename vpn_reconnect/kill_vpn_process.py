"""
Created on  Mar 12,  2016

:author: Shawn Li
:version: ff1

This file is for kill vpn process.
"""

# Import library for send CMD command
import os
# Get vpn check config parameters
from vpn_check_config_parser import *

# Kill vpn process by CMD command
def kill_process_by_name(process_name):
    # Make CMD command to kill vpn process
    cmd = "tskill %s" % process_name
    # send CMD command and get response
    result_info = os.system(cmd)
    print 'result_info = %d' % result_info
    print 'kill vpn process, result info=0, means ok, result info=0, means failed'
    # feedback return 0, process kill successfully
    if result_info == 0:
        print "exec \"%s\" success!!" % cmd
    # feedback return 1, process kill failed
    else:
        print "exec \"%s\" failed!!" % cmd

# Main func to debug
if __name__ == "__main__":

    kill_process_by_name(VPN_PROCESS_NAME)