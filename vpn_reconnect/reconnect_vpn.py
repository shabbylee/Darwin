"""
Created on  Mar 13,  2016

:author: Shawn Li
:version: ff1

This file is for reconnecting vpn connection.
"""

# Import library for send CMD command
import os
# Get vpn check config parameters
from vpn_check_config_parser import *
# Import library to wait time
import time
# Import check vpn status func
from check_vpn_status import *
# Import kill vpn process func
from kill_vpn_process import *
# Import log retry failed func
from vpn_retry_log import *


# Reconnect vpn func
def reconnect_vpn(exec_program_root, exec_program_name):
    # change work dir to vpn install folder
    os.chdir(exec_program_root)
    print os.getcwd()
    # start vpn exe file
    result = os.system('start ' + exec_program_name)
    print 'result = %d' % result
    print 'start vpn exe, result = 0, means ok, result = 0, means failed'
    if result == 0:
        print "Restart vpn successfully"
    else:
        print "Restart vpn failed"
    # wait 5 seconds for vpn connect successfully
    time.sleep(8)

# Main func
if __name__ == "__main__":
    # retry time = 3
    attempts = 0
    while attempts < RETRY_TIMES:
        # ping rackspace server ip to check vpn status
        vpn_status = check_vpn_status(RACKSPACE_SERVER_IP)
        print 'vpn_status = %d' % vpn_status
        print 'ping rackspace server ip, vpn_status=0, means ok, vpn_status=0, means failed'
        # rackspace server ip not connect
        if vpn_status == 1:
            attempts += 1
            print attempts
            if attempts == RETRY_TIMES:
                print 'Retry to Reconnect VPN 3 times Failed!'
                # log retry failed file
                log_retry_error_result = log_retry_error(RETRY_FAILED_LOG_PATH, RETRY_FAILED_LOG_NAME, RETRY_FAILED_LOG_MESSAGE)
                if log_retry_error_result:
                    print "Create Error Log File Successfully!"
                else:
                    print "Create Error Log File Failed!"

            else:
                print 'Reconnect VPN.'
                # kill vpn process
                kill_process_by_name(VPN_PROCESS_NAME)
                # restart vpn to reconnect
                reconnect_vpn(VPN_EXEC_ROOT, VPN_EXEC_NAME)
                # ping rackspace server ip again to check vpn status
                vpn_status_after_reconnect = check_vpn_status(RACKSPACE_SERVER_IP)
                # vpn status is connected
                if vpn_status_after_reconnect == 0:
                    print "Start VPN Successfully!!"
                # vpn status is not connected
                else:
                    print "Start VPN Failed!!"
        else:
                print "VPN Connection is Fine."
                print "Start RDPint.bat."
                os.system(RDPINIT_BAT_PATH)
                break


