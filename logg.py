# importing module
import logging

# Create and configure logger
'''
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
                    '''

# Creating an object
#logger = logging.getLogger()
#logger1 = logging.getLogger()

# Setting the threshold of logger to DEBUG
#logger.setLevel(logging.WARNING)
logger.setLevel(logging.ERROR)
#logger1.setLevel(logging.CRITICAL)

# Test messages
logger.debug("Harmless debug Message")
logger.debug("Hamless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

'''
msg = "Message"
    dict = {"k":"l"}
    list = [[]]
    logging.info('This is an info message from init \n %s',list) ot dict or msg
'''


'''
The default level is WARNING, 
which means that only events of this level and above will be tracked, 
unless the logging package is configured to do otherwise.
'''


'''
#logger requires StreamHandler(sys.stdout) to print INFO and DEBUG level info

logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)'''


'''
#logging.exception captures stack traces
import logging

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
  
except Exception as exception:
    logger.error('Failed to open file', exc_info=True)
    #gives with traceback
  
Output:
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]

'''








'''
Use rotating file handler

If you use FileHandler for writing logs, 
the size of the log file will grow with time. 
Someday, it will occupy all of your disk space. 
To avoid that situation, you should use RotatingFileHandler instead of FileHandler 
in the production environment.'''


'''
 Why working with the root logger for all modules isn’t the best idea??
That means, if you want to log the messages from myprojectmodule to one file 
and the logs from the main module in another file, root logger can’t that.'''


'''
While you can give pretty much any name to the logger, the convention is to use the __name__ variable like this:

logger = logging.getLogger(__name__)
logger.info('my logging message')

But, why use __name__ as the name of the logger, instead of hardcoding a name?

Because the __name__ variable will hold the name of the module (python file) that called the code. 
So, when used inside a module, it will create a logger bearing the value provided by the module’s __name__ attribute.

By doing this, if you end up changing module name (file name) in future, you don’t have to modify the internal code.
'''


'''
Formatting of message arguments is deferred until it cannot be avoided. 
However, computing the arguments passed to the logging method can also be expensive, and 
you may want to avoid doing it if the logger will just throw away your event. 
To decide what to do, you can call the isEnabledFor() method which takes a level argument and 
returns true if the event would be created by the Logger for that level of call. 
You can write code like this:

if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Message with %s, %s', expensive_func1(),
                                        expensive_func2())


Also note that the core logging module only includes the basic handlers. 
If you don’t import logging.handlers and logging.config, they won’t take up any memory.
'''

'''
The following useful handlers are provided in the package. 
Note that three of the handlers (StreamHandler, FileHandler and NullHandler) 
are actually defined in the logging module itself,

The other handlers are located in logging.handlers package

Using config file in logging requires logging.config package
'''

'''



    filemode='a', stream="yes")
  File "/usr/lib/python3.6/logging/__init__.py", line 1798, in basicConfig
    raise ValueError("'stream' and 'filename' should not be "
ValueError: 'stream' and 'filename' should not be specified together

'''