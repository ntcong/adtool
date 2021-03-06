#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import logging.handlers
from ui.mainWindow import MainWindow
import sys

from PySide import QtGui, QtCore
from ui.ListHandler import ListHandler


def main():

    logging.basicConfig(filename='adtool.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(name)s: %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filemode='w')
    # console = logging.StreamHandler()
    # console.setLevel(logging.ERROR)
    # console.setFormatter(logging.Formatter('%(name)-12s %(levelname) -8s: %(message)s'))
    log = logging.getLogger('adtool')
    # log.addHandler(console)
    handler = logging.handlers.RotatingFileHandler(
              'log/adtool.log', backupCount=50)
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname) -8s: %(message)s'))
    log.addHandler(handler)
    log.handlers[0].doRollover()
    log.info("Khởi động chương trình")
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
