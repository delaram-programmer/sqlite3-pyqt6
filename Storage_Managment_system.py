import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.QtGui import QPixmap
import sqlite3

class ButtonsScreen(QDialog):
    def __init__(self):
        super(ButtonsScreen,self).__init__()
        loadUi("button_window.ui", self)
        self.remaining.clicked.connect(self.remainingo)
        self.registered.clicked.connect(self.registeredo)
        self.report.clicked.connect(self.reports)
        self.workers.clicked.connect(self.workersfactors)
        self.rcustomers.clicked.connect(self.customers)

    def remainingo(self):
        mo = RemainingOrders
        widget.addWidget(mo)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def registeredo(self):
        go = RegisteredOrders
        widget.addWidget(go)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def reports(self):
        re = ReportsWindow
        widget.addWidget(re)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def workersfactors(self):
        wf = WorkersFactors
        widget.addWidget(wf)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def customers(self):
        rc = RegularCustomers
        widget.addWidget(rc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class RemainingOrders(QDialog):
    def __init__(self):
        super(RemainingOrders,self).__init__()
        loadUi("remaining_orders.ui", self)


class RegisteredOrders(QDialog):
    def __init__(self):
        super(RegisteredOrders,self).__init__()
        loadUi("registrered_orders.ui", self)

class ReportsWindow(QDialog):
    def __init__(self):
        super(ReportsWindow,self).__init__()
        loadUi("reports_window.ui", self)

class WorkersFactors(QDialog):
    def __init__(self):
        super(WorkersFactors,self).__init__()
        loadUi("workers_window.ui", self)

class RegularCustomers(QDialog):
    def __init__(self):
        super(RegularCustomers,self).__init__()
        loadUi("customers_window.ui", self)















app = QApplication(sys.argv)
allapp = ButtonsScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(allapp)
widget.setFixedHeight(400)
widget.setFixedWidth(530)
widget.show()

try:
    sys.exit(app.exec())
except Exception as e:
    print(f"Exiting: {e}")
