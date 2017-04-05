"""
Created on  Mar 12,  2016

:author: Shawn Li
:version: ff1

This file is for parsering vpn check config file to get configuration parameters.
"""
# Import config file parser library
import ConfigParser

config_parameters = ConfigParser.ConfigParser()
config_parameters.read("vpn_check_config.conf")

# Vpn check config info
RACKSPACE_SERVER_IP = config_parameters.get("vpn_config", "rackspace_server_ip")
VPN_PROCESS_NAME = config_parameters.get("vpn_config", "vpn_process_name")
VPN_EXEC_ROOT = config_parameters.get("vpn_config", "vpn_exec_root")
VPN_EXEC_NAME = config_parameters.get("vpn_config", "vpn_exec_name")
RDPINIT_BAT_PATH = config_parameters.get("vpn_config", "rdpinit_bat_path")
# Retry failed log info
RETRY_TIMES = config_parameters.getint("retry_failed_log", "retry_times")
RETRY_FAILED_LOG_PATH = config_parameters.get("retry_failed_log", "retry_failed_log_path")
RETRY_FAILED_LOG_NAME = config_parameters.get("retry_failed_log", "retry_failed_log_name")
RETRY_FAILED_LOG_MESSAGE = config_parameters.get("retry_failed_log", "retry_failed_log_message")
