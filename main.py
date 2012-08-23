#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtDeclarative import QDeclarativeView

# Create Qt application and the QDeclarative view
app = QtGui.QApplication(sys.argv)
view = QDeclarativeView()
# Create an URL to the QML file
url = QtCore.QUrl('view.qml')
# Set the QML file and show
view.setSource(url)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())