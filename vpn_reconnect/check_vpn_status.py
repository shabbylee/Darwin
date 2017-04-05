"""
Created on  Mar 27,  2016

:author: Shawn Li
:version: ff2

This file is for checking vpn status.
"""

# Import library for send CMD command
import os
import subprocess
# Get vpn check config parameters
from vpn_check_config_parser import *


# Check vpn status func
# PING Rackspace server ip to verify vpn connect or disconnect
def check_vpn_status(rackspace_server_ip):
    # # Solution 1
    # # Make CMD command to PING rackspace server ip
    # cmd = 'ping %s' % rackspace_server_ip
    # # send CMD command and get response
    # feedback_info = os.system(cmd)
    # # feedback return 0
    # if feedback_info == 0:
    #     # if 'Destination host unreachable' message contains in PING output, it means host machine physical connection is not good
    #     feedback_output = subprocess.Popen(["ping", rackspace_server_ip], stdout = subprocess.PIPE).communicate()[0]
    #     print feedback_output
    #     if 'Destination host unreachable' in feedback_output:
    #         print 'vpn disconnect, host machine physical connection is not good'
    #         feedback_info = 1
    #     else:
    #         print 'vpn connect'
    # # feedback return 1, vpn disconnect
    # else:
    #     print 'vpn disconnect, it can not reach the rackspace server'
    # # Return feedback info
    # print feedback_info
    # return feedback_info

    # Solution 2
    # output PING command information to verify network situation
    feedback_output = subprocess.Popen(["ping", rackspace_server_ip], stdout = subprocess.PIPE).communicate()[0]
    print feedback_output
    if 'TTL=' in feedback_output:
        print 'vpn connect'
        feedback_info = 0
    elif 'Destination host unreachable' in feedback_output:
        print 'vpn disconnect, host machine physical connection is not good'
        feedback_info = 1
    else:
        print 'vpn disconnect, it can not reach the rackspace server'
        feedback_info = 1

    print 'feedback_info = %d' % feedback_info
    print 'ping rackspace server ip, feedback info=0, means ok, feedback info=0, means failed'
    return feedback_info


# Main func to debug
if __name__ == '__main__':

    check_vpn_status(RACKSPACE_SERVER_IP)
