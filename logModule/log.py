#coding=utf-8

import logging
import os
import sys
import time

class realLog():
    def __init__(self, name, filePath):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.filePath = filePath
        self.__initLog()
        
    def __initLog(self):
        self.dateStr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.formatStr = logging.Formatter('[%(asctime)s] (%(levelname)s:%(message)s')
        logPath = self.filePath + '-' + self.dateStr + '.log'
        
        self.fileHandler = logging.FileHandler(logPath)
        self.fileHandler.setLevel(logging.DEBUG)
        self.fileHandler.setFormatter(self.formatStr)
        
        console = logging.StreamHandler()#输出到屏幕
        console.setFormatter(self.formatStr)
        
        self.logger.addHandler(self.fileHandler)
        self.logger.addHandler(console)
        
    def __updateHandler(self):   #  更新第二天的log
        currentDateStr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if currentDateStr != self.dateStr:
            self.dateStr = currentDateStr
            self.logger.removeHandler(self.fileHandler)
            # logPath = self.filePath + '-' + self.dateStr + '.log'
            logPath = self.filePath + '-' + self.dateStr + '.log'
            self.fileHandler = logging.FileHandler(logPath)
            self.fileHandler.setLevel(logging.DEBUG)
            self.fileHandler.setFormatter(self.formatStr)
            self.logger.addHandler(self.fileHandler)
            
    def debug(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.debug(msg, *args, **kwargs)
        except:
            pass
        
    def info(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.info(msg, *args, **kwargs)
        except:
            pass    
        
    def warning(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.warning(msg, *args, **kwargs)
        except:
            pass    
        
    def warn(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.warning(msg, *args, **kwargs)
        except:
            pass     
        
        
    def error(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.error(msg, *args, **kwargs)
        except:
            pass      
        
    def critical(self, msg, *args, **kwargs):
        try:
            self.__updateHandler()
            frame = sys._getframe(1)
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            msg = filename + ':' + str(lineno) + ') ' + str(msg)
            self.logger.critical(msg, *args, **kwargs)
        except:
            pass      
        
class Log(object):
    logDict = {}
    @staticmethod
    def getLogger(name):
        if name in Log.logDict:
            return Log.logDict[name]           # 在windows和Linux下的路径表示方式不同
        filePath = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'logs' + os.path.sep + 'task'
        # filePath = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + ' ../' + os.path.sep + 'log' + os.path.sep + name 
        # filePath = 'E:\00CodeFile\13PythonProgram\02log\logs\task'
        print("filepath:{}".format(filePath))
        myLog = realLog(name, filePath)
        Log.logDict[name] = myLog
        return myLog
        