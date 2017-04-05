"""
Created on  Feb 20,  2016

:author: Shawn Li

This file is for parsering email config file to get configuration parameters.
"""
# import config file parser library
import ConfigParser

config_parameters = ConfigParser.ConfigParser()
config_parameters.read("../email_config.conf")

# Email config info
EMAIL_SENDER = config_parameters.get("email_config", "email_sender")
EMAIL_RECEIVER_1 = config_parameters.get("email_config", "email_receiver_1")
EMAIL_RECEIVER_2 = config_parameters.get("email_config", "email_receiver_2")
EMAIL_RECEIVER_3 = config_parameters.get("email_config", "email_receiver_3")
EMAIL_SERVER = config_parameters.get("email_config", "email_server")
EMAIL_USER = config_parameters.get("email_config", "email_user")
EMAIL_PASSWORD = config_parameters.get("email_config", "email_password")

# Email content info
EMAIL_SUBJECT = config_parameters.get("email_content", "email_subject")
EMAIL_MESSAGES = config_parameters.get("email_content", "email_messages")

# Log file info
LOG_FILE_LOCATION = config_parameters.get("log_file", "log_file_location")
LOG_FILE_FILTER = config_parameters.get("log_file", "log_file_filter")