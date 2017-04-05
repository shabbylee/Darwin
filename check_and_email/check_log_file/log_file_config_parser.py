"""
Created on  Mar 6,  2016

:author: Shawn Li
:version: ff1

This file is for parsering log file config file to get configuration parameters.
"""
# import config file parser library
import ConfigParser

log_config_parameters = ConfigParser.ConfigParser()
log_config_parameters.read("../email_config.conf")

# Log file config info
LOG_FILE_LOCATION = log_config_parameters.get("log_file", "log_file_location")
LOG_FILE_FILTER = log_config_parameters.get("log_file", "log_file_filter")

