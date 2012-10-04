# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2011

@author: Fu4ny
'''
import logging


class ListHandler(logging.Handler):
    '''
    classdocs
    '''

    def __init__(self, level=logging.NOTSET, parent=None):
        '''
        Constructor
        '''
        logging.Handler.__init__(self, level)

    def emit(self, record):
        msg = self.format(record)
        self.func(msg)

    def guiHandler(self, func):
        self.func = func
