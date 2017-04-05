"""
Created on  Feb 20,  2016

:author: Shawn Li

This file is for sending notification email when check log file fail issue.
"""
# import email related library
from email.mime.text import MIMEText
from email.header import Header
import smtplib
# get email config parameters
from email_config_parser import *
# import check log file methods
from check_log_file.check_log_file import *
from check_log_file.get_local_time import *
# get log file config parameters
from check_log_file.log_file_config_parser import *

# Email parameters
email_sender = EMAIL_SENDER
email_receiver_1 = EMAIL_RECEIVER_1
email_receiver_2 = EMAIL_RECEIVER_2
email_receiver_3 = EMAIL_RECEIVER_3
email_server = EMAIL_SERVER
email_username = EMAIL_USER
email_password = EMAIL_PASSWORD
email_subject = EMAIL_SUBJECT
email_message = EMAIL_MESSAGES
emails_to_list = [email_receiver_1, email_receiver_2, email_receiver_3]

# Log file parameters
log_location = LOG_FILE_LOCATION
log_filter = LOG_FILE_FILTER
local_time = get_local_time()
log_keyword = local_time + '_Backups*.txt'


# Send email func
def send_mail(sender, receiver_list, subject, server, user, password, message):
    msg = MIMEText(message)
    msg['Subject'] = Header(subject)
    msg['From'] = sender
    msg['To'] = ";".join(receiver_list)

    try:
        email_service = smtplib.SMTP()
        email_service.connect(server)
        email_service.starttls()
        email_service.ehlo()
        email_service.login(user, password)
        email_service.sendmail(sender, receiver_list, msg.as_string())
        email_service.quit()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    # check present day log is missing or not
    if search_missing_file(log_location, log_keyword):
        # if present day log is existed, then check log file is failure or not
        if find_failure_log_files(log_location, log_filter):
            # log file is existed but failure
            print "Send log file is failure email!"
            failure_log_email_message = "%s_Backups-Failure.txt log file is a failure log file!" % local_time
            if send_mail(email_sender, emails_to_list, email_subject, email_server,\
                            email_username, email_password, failure_log_email_message):
                print "Email Send Successfully!"
            else:
                print "Email Send Failed!"
        else:
            # log file is existed and not failure
            print "Log file is existed and No failure today."

    else:
        # log file is missing
        print "Send log file is missing email!"
        missing_log_email_message = "%s_Backups.txt log file is missing!" % local_time
        if send_mail(email_sender, emails_to_list, email_subject, email_server,\
                        email_username, email_password, missing_log_email_message):
            print "Email Send Successfully!"
        else:
            print "Email Send Failed!"



