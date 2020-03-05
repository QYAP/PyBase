# coding:utf-8
'''
    @Author  : AP
    @Time    : 2019/9/3 22:18
    @File    : __init__.py.py
'''
# Copyright 2001-2016 by Vinay Sajip. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""
Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2016 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!
"""

import sys, os, time, io, traceback, warnings, weakref, collections

from string import Template

__all__ = [
    'BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Formatter',
    'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'NOTSET', 'NullHandler', 'StreamHandler', 'WARN', 'WARNING',
    'addLevelName', 'basicConfig', 'captureWarnings', 'critical', 'debug', 'disable', 'error', 'exception', 'fatal',
    'getLevelName', 'getLogger', 'getLoggerClass', 'info', 'log', 'makeLogRecord', 'setLoggerClass', 'shutdown', 'warn',
    'warning', 'getLogRecordFactory', 'setLogRecordFactory', 'lastResort', 'raiseExceptions'
]

try:
    import threading
except ImportError:  #pragma: no cover
    threading = None

__author__ = "Vinay Sajip <vinay_sajip@red-dove.com>"
__status__ = "production"
# The following module attributes are no longer updated.
__version__ = "0.5.1.2"
__date__ = "07 February 2010"

#---------------------------------------------------------------------------
#   Miscellaneous module data
#---------------------------------------------------------------------------

#
#_startTime is used as the base when calculating the relative time of events
#
_startTime = time.time()

#
#raiseExceptions is used to see if exceptions during handling should be
#propagated
#
raiseExceptions = True

#
# If you don't want threading information in the log, set this to zero
#
logThreads = True

#
# If you don't want multiprocessing information in the log, set this to zero
#
logMultiprocessing = True

#
# If you don't want process information in the log, set this to zero
#
logProcesses = True

#---------------------------------------------------------------------------
#   Level related stuff
#---------------------------------------------------------------------------
#
# Default levels and level names, these can be replaced with any positive set
# of values having corresponding names. There is a pseudo-level, NOTSET, which
# is only really there as a lower limit for user-defined levels. Handlers and
# loggers are initialized with NOTSET so that they will log all messages, even
# at user-defined levels.
#

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}


def getLevelName(level):
    """
    Return the textual representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    Otherwise, the string "Level %s" % level is returned.
    """
    # See Issues #22386, #27937 and #29220 for why it's this way
    result = _levelToName.get(level)
    if result is not None:
        return result
    result = _nameToLevel.get(level)
    if result is not None:
        return result
    return "Level %s" % level


def addLevelName(level, levelName):
    """
    Associate 'levelName' with 'level'.

    This is used when converting levels to text during message formatting.
    """
    _acquireLock()
    try:  #unlikely to cause an exception, but you never know...
        _levelToName[level] = levelName
        _nameToLevel[levelName] = level
    finally:
        _releaseLock()


if hasattr(sys, '_getframe'):
    currentframe = lambda: sys._getframe(3)
else:  #pragma: no cover

    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back
currentframe()