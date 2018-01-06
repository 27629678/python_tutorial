# Logging
# Purpose: Record progress and problems ...
# Levels: Debug, Info, Warning, Error, Critical

import logging

dir(logging)

# ['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'H
# andler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PlaceHolder', 'RootLogger', 'StreamH
# andler', 'WARN', 'WARNING', '__all__', '__author__', '__builtins__', '__date__', '__doc__', '__file__', '__name__', '__package__',
#  '__path__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_handlerList', '_
# handlers', '_levelNames', '_lock', '_loggerClass', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime',
# '_unicode', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'cStringIO', 'captureWarnings', 'codecs', 'collectio
# ns', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogger', 'getLoggerClass',
#  'info', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 'root', 'setLoggerCl
# ass', 'shutdown', 'sys', 'thread', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="D:\\log\\lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')

logger = logging.getLogger()
print("logger level: ", logger.level)

logger.info("hello, world.")
