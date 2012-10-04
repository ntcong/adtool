# coding=utf-8
#log=logging.getLogger('MainWindow')

#from PySide.QtUiTools import *
from PySide import QtGui, QtCore
from adtool_ui import Ui_ADTool
import active_directory
import pywintypes
import datetime
from ListHandler import ListHandler
import logging

VERSION = 'v2.1'
RELEASE_DATE = '04/10/2012'
log = logging.getLogger('adtool')


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        #super(MainWindow, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.ui = Ui_ADTool()
        self.ui.setupUi(self)
        self.setWindowTitle("AD Tool")
        self.set_password()
        listLog = ListHandler()
        listLog.guiHandler(self.addLog)
        listLog.setFormatter(logging.Formatter('%(name)-12s %(levelname) -8s: %(message)s'))
        logging.getLogger('').addHandler(listLog)
        #connect button
        self.connect(self.ui.checkacc_button, \
                        QtCore.SIGNAL('clicked()'), self.check_account)
        self.connect(self.ui.disable_button, \
                        QtCore.SIGNAL('clicked()'), self.disable_account)
        self.connect(self.ui.resetpwd_button, \
                        QtCore.SIGNAL('clicked()'), self.reset_password)
        self.connect(self.ui.unlock_button, \
                        QtCore.SIGNAL('clicked()'), self.unlock_account)
        self.connect(self.ui.extend_button, \
                        QtCore.SIGNAL('clicked()'), self.extend_account)
        self.connect(self.ui.acclist_textbox, \
                        QtCore.SIGNAL('editingFinished()'), self.acclist_check)
        self.connect(self.ui.date_textbox, \
                        QtCore.SIGNAL('editingFinished()'), self.check_date_textbox)
        self.connect(self.ui.extend_date, \
                        QtCore.SIGNAL('editingFinished()'), self.check_extend_date)
        self.connect(self.ui.targetou_textbox, \
                        QtCore.SIGNAL('editingFinished()'), self.check_OU)
        self.connect(self.ui.defaultpwd_textbox, \
                        QtCore.SIGNAL('editingFinished()'), self.set_password)

        self.ui.date_textbox.setText(self.get_date().strftime('%d/%m/%Y'))
        self.ui.extend_date.setText(self.get_extend_date().strftime('%d/%m/%Y'))
        self.change_targetou(self.get_date()[1], self.get_date()[2])
        self.ui.version_info.setText('%s %s by CongNT3' % (VERSION, RELEASE_DATE))
        #self.check_OU()
        self.ui.acctable_widget.horizontalHeader().resizeSection(0, 100)
        self.ui.acctable_widget.horizontalHeader().resizeSection(2, 110)
        self.ui.acctable_widget.horizontalHeader().resizeSection(3, 200)
        self.ui.acctable_widget.horizontalHeader().resizeSection(4, 350)
        self.ui.acctable_widget.horizontalHeader().resizeSection(5, 20)
        self.ui.acctable_widget.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.Fixed)
        headers = self.ui.acctable_widget.horizontalHeader()
        headers.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        headers.customContextMenuRequested.connect(self.header_popup)

    def addLog(self, message):
        self.ui.log_widget.addItem(message)
        self.ui.log_widget.setCurrentRow(self.ui.log_widget.count() - 1, QtGui.QItemSelectionModel.Current)

    def header_popup(self, pos):
        menu = QtGui.QMenu()
        menu_checked = QtGui.QMenu('Check')
        menu_uncheck = QtGui.QMenu('Uncheck')
        menu.addMenu(menu_checked)
        menu.addMenu(menu_uncheck)
        check_all = menu_checked.addAction("Check All")
        check_valid = menu_checked.addAction("Check all Valid account")
        check_invalid = menu_checked.addAction("Check all Invalid account")
        check_ok = menu_checked.addAction("Check all OK account")
        check_locked = menu_checked.addAction("Check all Locked account")
        check_disabled = menu_checked.addAction("Check all Disabled account")
        check_expired = menu_checked.addAction("Check all Expired account")

        uncheck_all = menu_uncheck.addAction("Uncheck All")
        uncheck_valid = menu_uncheck.addAction("Uncheck all Valid account")
        uncheck_invalid = menu_uncheck.addAction("Uncheck all Invalid account")
        uncheck_ok = menu_uncheck.addAction("Uncheck all OK account")
        uncheck_locked = menu_uncheck.addAction("Uncheck all Locked account")
        uncheck_disabled = menu_uncheck.addAction("Uncheck all Disabled account")
        uncheck_expired = menu_uncheck.addAction("Uncheck all Expired account")
        action = menu.exec_(self.ui.acctable_widget.mapToGlobal(pos))
        if action == check_all:
            self.table_check()
        elif action == uncheck_all:
            self.table_uncheck()
        elif action == check_disabled:
            self.table_check(self.table_filter('DISABLED'))
        elif action == uncheck_disabled:
            self.table_uncheck(self.table_filter('DISABLED'))
        elif action == check_ok:
            self.table_check(self.table_filter('OK'))
        elif action == uncheck_ok:
            self.table_uncheck(self.table_filter('OK'))
        elif action == check_locked:
            self.table_check(self.table_filter('LOCKED'))
        elif action == uncheck_locked:
            self.table_uncheck(self.table_filter('LOCKED'))
        elif action == check_valid:
            self.table_check(self.table_filter('valid'))
        elif action == uncheck_valid:
            self.table_uncheck(self.table_filter('valid'))
        elif action == check_expired:
            self.table_check(self.table_filter('EXPIRED'))
        elif action == uncheck_expired:
            self.table_uncheck(self.table_filter('EXPIRED'))
        elif action == check_invalid:
            self.table_check(self.table_filter('NOT FOUND'))
        elif action == uncheck_invalid:
            self.table_uncheck(self.table_filter('NOT FOUND'))

    def extend_account(self, user=None):
        if user != None:
            user_checked = [user]
        else:
            user_checked = self.get_checked_table()
        reply = QtGui.QMessageBox.question(self, 'Extend Account',
            u'Gia hạn các account đã đánh dấu?', QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No,  QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            date = self.get_extend_date()
            date_string = ''
            if date != '0':
                date = [int(i) for i in date]
                date.reverse()
                date = datetime.datetime(*date)
                date_string = date.strftime('%d/%m/%Y')
            else:
                date = datetime.datetime(1970, 1, 1, 0, 0)
                date_string = u'Không hết hạn'
            log.info(u'Đặt các user: %s' % [str(i) for i in user_checked])
            log.info(u'ngày hết hạn: %s' % date_string)

            try:
                for user in user_checked:
                    user_object = active_directory.AD_object("LDAP://%s" % user)
                    user_object.com_object.AccountExpirationDate = date
                    user_object.SetInfo()
                    log.info(u'User: %s! DONE' % user)
            except pywintypes.com_error:
                QtGui.QMessageBox.critical(self, u'Authentication Error', u'Account đang sử dụng không có đủ quyền hạn')
                return

            log.info(u'Hoàn tất')
            self.check_account()

    def set_password(self):
        self.default_password = self.ui.defaultpwd_textbox.text()

    def change_targetou(self, month, year):
        targetou = "OU=Thang %s,OU=Nam %s,OU=Hanoi,OU=NghiViec,DC=HO,DC=FPT,DC=VN" % (month, year)
        self.ui.targetou_textbox.setText(targetou)

    def get_date(self, str=None):
        if str == None:
            if self.ui.date_textbox.text() == '':
                now = datetime.datetime.now()
                return now
            else:
                return self.get_date(self.ui.date_textbox.text())
        else:
            #dd/mm/yyyy
            return str[:2], str[3:5], str[6:]

    def get_extend_date(self, str=None):
        if str == None:
            if self.ui.extend_date.text() == '':
                now = datetime.datetime.now()
                return now
            else:
                return self.get_extend_date(self.ui.extend_date.text())
        else:
            #dd/mm/yyyy
            if str == '0':
                return '0'  # no expires date
            else:
                return str[:2], str[3:5], str[6:]

    def is_locked(self, acc='', user=None):
        if user is None:
            user = active_directory.find_user(acc)
        return 'ADS_UF_LOCKOUT' in user.userAccountControl

    def is_disabled(self, acc='', user=None):
        if user is None:
            user = active_directory.find_user(acc)
        return 'ADS_UF_ACCOUNTDISABLE' in user.userAccountControl

    def get_groups(self, user):
        result = ""
        for group in user.memberOf:
            result += '%s; ' % group.cn
        return result

    def get_acc_expires(self, user):
        try:
            date = user.accountExpires
            date += datetime.timedelta(0, 25629, 496730)
            return date.strftime('%d/%m/%Y')
        except (ValueError, OverflowError):
            return "NO EXPIRES"

    def is_expired(self, user):
        if self.get_acc_expires(user) == "NO EXPIRES":
            return False
        return user.accountExpires < datetime.datetime.now()

    def check_account(self):
        '''
        Get the account list in checkbox and show the information
        '''
        if not self.check_date_textbox():
            return
        if not self.check_extend_date():
            return
        reload(active_directory)  # reload because of COM object caching
        self.ui.acctable_widget.setRowCount(0)
        #self.ui.acctable_widget.clear()
        account_list = self.ui.acclist_textbox.toPlainText()
        if account_list == None or account_list == '':
            QtGui.QMessageBox.critical(self, u'Input Error', u'Nhập danh sách account trước')
            return
        #make the account list separator is white space to split
        account_list = account_list.replace(';', ' ')
        account_list = account_list.replace(',', ' ')
        account_list = account_list.split()
        log.info(u'Scan danh sách account %s' % [str(i) for i in account_list])
        for acc in account_list:
            try:
                user = active_directory.find_user(acc)
            except:
                user = None
            if user != None:
                status = ''
                color = None
                checked = False
                status = 'OK'
                if self.is_locked(user=user):
                    status = 'LOCKED'
                    color = QtGui.QColor(0, 0, 255)
                    checked = False
                if self.is_expired(user):
                    status = 'EXPIRED'
                    color = QtGui.QColor(0, 255, 0)
                    checked = False
                if self.is_disabled(user=user):
                    status = 'DISABLED'
                    color = QtGui.QColor(0, 0, 255)
                    checked = False
                self.add_item_table(acc, status, self.get_acc_expires(user), self.get_groups(user), user.distinguishedName, checked, color)
            else:
                self.add_item_table(acc, status='NOT FOUND', checked=False, color=QtGui.QColor(255, 0, 0))
        log.info(u'Hoàn tất')

    def disable_account(self):
        user_checked = self.get_checked_table()
        reply = QtGui.QMessageBox.question(self, 'Disable Account',
            u'Disable account đã đánh dấu?', QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No,  QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            target_ou = self.check_OU()
            if target_ou != None:
                destination_ou = active_directory.AD_object("LDAP://%s" % target_ou)
                log.info(u'Move các user: %s' % [str(i) for i in user_checked])
                log.info(u' từ %s đến %s' % (target_ou, destination_ou))
                try:
                    for user in user_checked:
                        user_object = active_directory.AD_object("LDAP://%s" % user)
                        user_object.description = 'Disable %s/%s/%s' % self.get_date()
                        user_object.AccountDisabled = True
                        user_object.userAccountControl.update('ADS_UF_ACCOUNTDISABLE')
                        user_object.com_object.AccountDisabled = True
                        user_object.SetInfo()
                        log.info(u'User: %s! DONE' % user)
                        destination_ou.com_object.MoveHere(str(user_object.as_string()), str(user_object.Name))
                except pywintypes.com_error:
                    QtGui.QMessageBox.critical(self, u'Authentication Error', u'Account đang sử dụng không có đủ quyền hạn')
                    return
            log.info(u'Hoàn tất')
            self.check_account()

    def reset_password(self):
        user_checked = self.get_checked_table()
        new_password = self.ui.defaultpwd_textbox.text()
        reply = QtGui.QMessageBox.question(self, 'Reset Password',
            u'Reset mật khẩu user đã đánh dấu về %s?' % new_password, QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            log.info(u'Reset mật khẩu các user %s thành %s' % ([str(i) for i in user_checked], new_password))
            try:
                for user in user_checked:
                    user_object = active_directory.AD_object("LDAP://%s" % user)
                    user_object.SetPassword(new_password)
                    log.info(u'User: %s! DONE' % user)
            except pywintypes.com_error:
                QtGui.QMessageBox.critical(self, u'Authentication Error', u'Account đang sử dụng không có đủ quyền hạn')
                return
            log.info(u'Hoàn tất')
            self.check_account()

    def unlock_account(self):
        #ADS_UF_LOCKOUT
        user_checked = self.get_checked_table()
        reply = QtGui.QMessageBox.question(self, 'Unlock Account',
            u'Unlock account đã đánh dấu?', QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            log.info(u'Unlock các user: %s' % [str(i) for i in user_checked])
            try:
                for user in user_checked:
                    user_object = active_directory.AD_object("LDAP://%s" % user)
                    if 'ADS_UF_LOCKOUT' in user_object.userAccountControl:
                            user_object.userAccountControl.remove('ADS_UF_LOCKOUT')
                            log.info('User: %s! DONE' % user)
            except pywintypes.com_error:
                QtGui.QMessageBox.critical(self, u'Authentication Error', u'Account đang sử dụng không có đủ quyền hạn')
                return
            log.info(u'Hoàn tất')
            self.check_account()

    def acclist_check(self):
        pass

    def check_date_textbox(self):
        success = True
        text = self.ui.date_textbox.text()
        if len(text) != 10:
            success = False
        try:
            day = int(text[:2])
            month = int(text[3:5])
            year = int(text[6:])
            if not 1 <= day <= 31 or not 1 <= month <= 12 or not 2000 <= year <= 3000:
                success = False
        except ValueError:
            success = False
        if not success:
            QtGui.QMessageBox.critical(self, u'Input Error', u'Ngày tháng không hợp lệ')
            self.ui.date_textbox.setFocus()

        return success

    def check_extend_date(self):
        success = True
        text = self.ui.extend_date.text()
        if text == '0':
            return True
        if len(text) != 10:
            success = False
        try:
            day = int(text[:2])
            month = int(text[3:5])
            year = int(text[6:])
            if not 1 <= day <= 31 or not 1 <= month <= 12 or not 1000 <= year <= 3000:
                success = False
        except ValueError:
            success = False
        if not success:
            QtGui.QMessageBox.critical(self, u'Input Error', u'Ngày tháng không hợp lệ')
            self.ui.extend_date.setFocus()
        return success

    def check_OU(self):
        # destination_ou = active_directory.AD_object("LDAP://OU=Thang 08,OU=Nam 2012,OU=Hanoi,OU=NghiViec,DC=HO,DC=FPT,DC=VN")
        try:
            ou = self.ui.targetou_textbox.text()
            destination_ou = active_directory.AD_object("LDAP://%s" % ou)
            if destination_ou.ou == None or destination_ou.ou == '':
                raise Exception
            return ou
        except Exception:
            QtGui.QMessageBox.critical(self, u'Input Error', u'OU không hợp lệ hoặc không tồn tại')
            self.ui.targetou_textbox.setFocus()
            return None

    def get_checked_table(self, status=None):
        table = self.ui.acctable_widget
        rows = table.rowCount()
        result = []
        for row in range(rows):
            #DN: table[2], checked: table[3]
            if table.item(row, 5).checkState() == QtCore.Qt.CheckState.Checked:
                if status == None:
                    result.append(table.item(row, 4).text())
                elif status == 'valid' and table.item(row, 1).text() != 'NOT FOUND':
                    result.append(table.item(row, 4).text())
                elif table.item(row, 1).text() == status:
                    result.append(table.item(row, 4).text())
        return result

    def table_filter(self, status=None):
        table = self.ui.acctable_widget
        rows = table.rowCount()
        result = []
        for row in range(rows):
            #DN: table[2], checked: table[3]
            if status == None or status == '':
                result.append(table.item(row, 0).text())
            elif status == 'valid' and table.item(row, 1).text() != 'NOT FOUND':
                result.append(table.item(row, 0).text())
            elif table.item(row, 1).text() == status:
                result.append(table.item(row, 0).text())
        return result

    def table_check(self, acc_list=None):
        table = self.ui.acctable_widget
        rows = table.rowCount()
        for row in range(rows):
            #table.item(row)
            if acc_list == None or table.item(row, 0).text() in acc_list:
                table.item(row, 5).setCheckState(QtCore.Qt.CheckState.Checked)

    def table_uncheck(self, acc_list=None):
        table = self.ui.acctable_widget
        rows = table.rowCount()
        for row in range(rows):
            #table.item(row)
            if acc_list == None or table.item(row, 0).text() in acc_list:
                table.item(row, 5).setCheckState(QtCore.Qt.CheckState.Unchecked)

    def add_item_table(self, acc, status, expires='', groups='', dn='', checked=True, color=None):
        # items=[QtGui.QtGui.QTableWidgetItem(ip),
        # QtGui.QtGui.QTableWidgetItem(mac),QtGui.QtGui.QTableWidgetItem(hostname)]
        #     if ip==self.gw['gw']:
        #         items.append(QtGui.QtGui.QTableWidgetItem(u'Gateway'))
        row = self.ui.acctable_widget.rowCount()
        self.ui.acctable_widget.setRowCount(row + 1)
        items = [QtGui.QTableWidgetItem(acc), QtGui.QTableWidgetItem(status), \
                QtGui.QTableWidgetItem(expires), QtGui.QTableWidgetItem(groups), QtGui.QTableWidgetItem(dn)]
        item = QtGui.QTableWidgetItem()
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        elif self.ui.acctable_widget.item(row, 5) != None:
            item.setCheckState(self.ui.acctable_widget.item(row, 5).CheckState())
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
        items.append(item)
        for i in range(len(items)):
            item = items[i]
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.ui.acctable_widget.setItem(row, i, item)
        if color != None:
            self.ui.acctable_widget.item(row, 1).setBackground(color)
