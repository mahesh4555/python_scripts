#CODE1
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -  %(levelname)s - %(message)s', filename='lavazza.log', filemode='a' )

logging.info("Provision completed")
logging.warning("Diagnostics collection incomplete")
logging.error("Keep alive msg not sending")
logging.warning("Server communication response sent, but not updates")
logging.critical("Device config File not found")

#OUTPUT1:
2020-04-30 10:06:28,242 -  INFO - Provision completed
2020-04-30 10:06:28,242 -  WARNING - Diagnostics collection incomplete
2020-04-30 10:06:28,242 -  ERROR - Keep alive msg not sending
2020-04-30 10:06:28,242 -  WARNING - Server communication response sent, but not updates
2020-04-30 10:06:28,242 -  CRITICAL - Device config File not found


#CODE2
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - GUI - %(levelname)s - %(message)s', filename='lavazza.log', filemode='a' )

logging.info("Provision completed")
logging.critical("gui config File not found")

#OUTPUT2:
2020-04-30 10:08:18,484 - GUI - INFO - Provision completed
2020-04-30 10:08:18,485 - GUI - CRITICAL - gui config File not found


#CODE3
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - PUBSUB - %(levelname)s - %(message)s', filename='lavazza.log', filemode='a' )

logging.info("Async pull subscription succes")
logging.critical("Sync pull subscription failed")
logging.debug("HTTP POST request sent")

#OUTPUT3:
2020-04-30 10:11:56,313 - PUBSUB - INFO - Async pull subscription succes
2020-04-30 10:11:56,313 - PUBSUB - CRITICAL - Sync pull subscription failed
2020-04-30 10:11:56,314 - PUBSUB - DEBUG - HTTP POST request sent


#CODE4
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(module_name)s- %(levelname)s - %(message)s',filename='lavazza.log', filemode='a')

logging.info("Provision completed", extra={'module_name': 'GUI'})
logging.error("Subscription error", extra={'module_name': 'PUBSUB'})
logging.warning("Diagnostics collection incomplete", extra={'module_name': 'DIAGNOSTICS'})
logging.warning("Server communication response sent, but not updates", extra={'module_name': 'SERVER_COMMUNICATION'})
logging.critical(" config File not found", extra={'module_name': 'GUI'})
logging.error('Keep alive msg not sending', extra={'module_name': 'KEEP_ALIVE'})


#OUTPUT4:
2020-04-30 10:16:48,304 - GUI- INFO - Provision completed
2020-04-30 10:16:48,304 - PUBSUB- ERROR - Subscription error
2020-04-30 10:16:48,304 - DIAGNOSTICS- WARNING - Diagnostics collection incomplete
2020-04-30 10:16:48,305 - SERVER_COMMUNICATION- WARNING - Server communication response sent, but not updates
2020-04-30 10:16:48,305 - GUI- CRITICAL -  config File not found
2020-04-30 10:16:48,305 - KEEP_ALIVE- ERROR - Keep alive msg not sending


#CODE 5
import logging
logger=logging.getLogger()
logger.setLevel(logging.ERROR)

file_handler=logging.FileHandler('lavazza.log')
file_formatter=logging.Formatter("{'time':'%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'}")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logging.info("Provision completed")
logging.warning("Diagnostics collection incomplete")
logging.error("Keep alive msg not sending")
logging.warning("Server communication response sent, but not updates")
logging.critical("Device config File not found")

#OUTPUT5:
{'time':'2020-05-05 16:49:38,485', 'level': 'ERROR', 'message': 'Keep alive msg not sending'}
{'time':'2020-05-05 16:49:38,485', 'level': 'CRITICAL', 'message': 'Device config File not found'}

#CODE 6
import logging
logger=logging.getLogger()
#need to setlevel, else it captures only level greater than
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler('lavazza.log')
file_formatter=logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s','module_name': '%(module_name)s', 'message': '%(message)s'}")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logging.info("Provision completed", extra={'module_name': 'GUI'})
logging.warning("Diagnostics collection incomplete", extra={'module_name': 'DIAGNOSTICS'})
logging.error("Keep alive msg not sending", extra={'module_name': 'KEEP_ALIVE'})
logging.warning("Server communication response sent, but not updates", extra={'module_name': 'SERVER_COMM'})
logging.critical("Device config File not found", extra={'module_name': 'GUI'})


#OUTPUT6:
{'time':'2020-05-05 16:56:19,603', 'level': 'INFO','module_name': 'GUI', 'message': 'Provision completed'}
{'time':'2020-05-05 16:56:19,603', 'level': 'WARNING','module_name': 'DIAGNOSTICS', 'message': 'Diagnostics collection incomplete'}
{'time':'2020-05-05 16:56:19,603', 'level': 'ERROR','module_name': 'KEEP_ALIVE', 'message': 'Keep alive msg not sending'}
{'time':'2020-05-05 16:56:19,603', 'level': 'WARNING','module_name': 'SERVER_COMM', 'message': 'Server communication response sent, but not updates'}
{'time':'2020-05-05 16:56:19,603', 'level': 'CRITICAL','module_name': 'GUI', 'message': 'Device config File not found'}

#CODE7
import logging
logger=logging.getLogger()
#need to setlevel, else it captures only level greater than
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler('lavazza.log')
file_formatter=logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s','module_name': '%(module_name)s', 'message': '%(message)s'}")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logging.info("Provision completed", extra={'module_name': 'GUI'})
logging.warning("Diagnostics collection incomplete", extra={'module_name': 'DIAGNOSTICS'})
logging.error("Keep alive msg not sending", extra={'module_name': 'KEEP_ALIVE'})
logging.warning("Server communication response sent, but not updates", extra={'module_name': 'SERVER_COMM'})
logging.critical("Device config File not found", extra={'module_name': 'GUI'})


def a():
    try:
        a = 1 / 0
    except:
        logging.exception("Exception in a:1/0",extra={'module_name': 'GUI'})
a()

#OUTPUT7
{'time':'2020-05-05 17:25:08,340', 'level': 'INFO','module_name': 'GUI', 'message': 'Provision completed'}
{'time':'2020-05-05 17:25:08,340', 'level': 'WARNING','module_name': 'DIAGNOSTICS', 'message': 'Diagnostics collection incomplete'}
{'time':'2020-05-05 17:25:08,340', 'level': 'ERROR','module_name': 'KEEP_ALIVE', 'message': 'Keep alive msg not sending'}
{'time':'2020-05-05 17:25:08,340', 'level': 'WARNING','module_name': 'SERVER_COMM', 'message': 'Server communication response sent, but not updates'}
{'time':'2020-05-05 17:25:08,340', 'level': 'CRITICAL','module_name': 'GUI', 'message': 'Device config File not found'}
{'time':'2020-05-05 17:25:08,340', 'level': 'ERROR','module_name': 'GUI', 'message': 'Exception in a:1/0'}
Traceback (most recent call last):
  File "/home/pi/lavazza/src/source_code/features/DIAGNOSTICS/logg10.py", line 22, in a
    a = 1 / 0
ZeroDivisionError: division by zero

    
    
#CODE9
#Using log_level as variable


import logging

#**********************

log_level = logging.INFO
log_format = '%(asctime)s - DIAGNSOTICS - %(levelname)s - %(message)s'

#***********************
print(type(log_level))
print(log_level)
logging.basicConfig(level=log_level, format=log_format)

logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("Careful! Something does not look right")
logging.error("You have encountered an error")
logging.critical("You are in trouble")

#OUTPUT9
2020-07-10 20:30:39,757 - DIAGNSOTICS - INFO - This is an informational message
2020-07-10 20:30:39,757 - DIAGNSOTICS - WARNING - Careful! Something does not look right
2020-07-10 20:30:39,757 - DIAGNSOTICS - ERROR - You have encountered an error
2020-07-10 20:30:39,757 - DIAGNSOTICS - CRITICAL - You are in trouble

