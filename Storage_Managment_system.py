import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget , QPushButton
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class ButtonsScreen(QMainWindow):
    def __init__(self):
        super(ButtonsScreen, self).__init__()
        loadUi("button_window.ui", self)
        self.remaining.clicked.connect(self.remainingo)
        self.registered.clicked.connect(self.registeredo)
        self.report.clicked.connect(self.reports)
        self.workers.clicked.connect(self.workersfactors)
        self.rcustomers.clicked.connect(self.customers)

    def remainingo(self):
        try:
            mo = RemainingOrders()
            widget.addWidget(mo)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(f"Error in remainingo: {e}")

    def registeredo(self):
        try:
            go = RegisteredOrders()
            widget.addWidget(go)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(f"Error in registeredo: {e}")

    def reports(self):
        try:
            re = ReportsWindow()
            widget.addWidget(re)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(f"Error in reports: {e}")

    def workersfactors(self):
        try:
            wf = WorkersFactors()
            widget.addWidget(wf)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(f"Error in workersfactors: {e}")

    def customers(self):
        try:
            rc = RegularCustomers()
            widget.addWidget(rc)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(f"Error in customers: {e}")




class RemainingOrders(QMainWindow):
    def __init__(self):
        super(RemainingOrders, self).__init__()
        loadUi("remaining_orders.ui", self)


        self.setWindowTitle("Remaining Orders")
        self.setGeometry(100, 100, 600, 400)


        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.load_remaining_orders()
    def load_remaining_orders(self):
        try:
            connection1 = sqlite3.connect("Storage_Managment_Data.db")
            cursor1 = connection1.cursor()

            cursor1.execute("""CREATE TABLE IF NOT EXISTS Remainings(
                        AcceptanceDate TEXT NOT NULL,
                        OrderName TEXT PRIMARY KEY NOT NULL,
                        RequiredMaterials TEXT NOT NULL,
                        DeliveryDate TEXT NOT NULL
                        );
                        """)


            cursor1.execute("SELECT * FROM Remainings")
            rows = cursor1.fetchall()


            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(4)


            self.table_widget.setHorizontalHeaderLabels(["Acceptance Date", "Order Name", "Required Materials", "Delivery Date"])


            self.table_widget.setColumnWidth(0, 100)  # Acceptance Date
            self.table_widget.setColumnWidth(1, 150)  # Order Name
            self.table_widget.setColumnWidth(2, 200)  # Required Materials
            self.table_widget.setColumnWidth(3, 100)  # Delivery Date


            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

            connection1.commit()
        except Exception as e:
            print("Database error: " + str(e))
        finally:
            connection1.close()




class RegisteredOrders(QMainWindow):
    def __init__(self):
        super(RegisteredOrders, self).__init__()
        loadUi("registered_orders.ui", self)

        self.setWindowTitle("Registered Orders")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.load_registered_orders()

    def go_to_main_screen(self):
        widget.setCurrentIndex(0)


    def load_registered_orders(self):
        try:
            connection1 = sqlite3.connect("Storage_Managment_Data.db")
            cursor1 = connection1.cursor()

            cursor1.execute("""CREATE TABLE IF NOT EXISTS Registereds(
                        AcceptanceDate TEXT NOT NULL,
                        OrderName TEXT PRIMARY KEY NOT NULL,
                        RequiredMaterials TEXT NOT NULL,
                        DeliveryDate TEXT NOT NULL
                        );
                        """)
            connection1.commit()

            cursor1.execute("SELECT * FROM Registereds")
            rows = cursor1.fetchall()

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(4)
            self.table_widget.setHorizontalHeaderLabels(["Acceptance Date", "Order Name", "Required Materials", "Delivery Date"])

            self.table_widget.setColumnWidth(0, 100)  # Acceptance Date
            self.table_widget.setColumnWidth(1, 150)  # Order Name
            self.table_widget.setColumnWidth(2, 200)  # Required Materials
            self.table_widget.setColumnWidth(3, 100)  # Delivery Date

            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

            connection1.commit()
        except Exception as e:
            print("Database error: " + str(e))
        finally:
            connection1.close()




class ReportsWindow(QMainWindow):
    def __init__(self):
        super(ReportsWindow, self).__init__()
        loadUi("reports_window.ui", self)

        self.setWindowTitle("Reports")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.load_reports()
    def load_reports(self):
        try:
            connection1 = sqlite3.connect("Storage_Managment_Data.db")
            cursor1 = connection1.cursor()

            cursor1.execute("""CREATE TABLE IF NOT EXISTS Reports(
                        AvailableMaterials TEXT NOT NULL,
                        FinishedMaterials TEXT NOT NULL,
                        ProfitOrders TEXT NOT NULL
                            );
                            """)
            connection1.commit()

            cursor1.execute("SELECT * FROM Reports")
            rows = cursor1.fetchall()

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(3)
            self.table_widget.setHorizontalHeaderLabels(
                ["Available Materials", "Finished Materials", "Profit Orders"])

            self.table_widget.setColumnWidth(0, 150)  # Available Materials
            self.table_widget.setColumnWidth(1, 150)  # Finished Materials
            self.table_widget.setColumnWidth(2, 200)  # Profit Orders

            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

                connection1.commit()
        except Exception as e:
            print("Database error: " + str(e))
        finally:
            connection1.close()




class WorkersFactors(QMainWindow):
    def __init__(self):
        super(WorkersFactors, self).__init__()
        loadUi("workers_window.ui", self)

        self.setWindowTitle("Workers-Factors")
        self.setGeometry(100, 100, 650, 450)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.load_workers()

    def load_workers(self):
        try:
            connection1 = sqlite3.connect("Storage_Managment_Data.db")
            cursor1 = connection1.cursor()

            cursor1.execute("""CREATE TABLE IF NOT EXISTS Workers(
                        FirstName TEXT NOT NULL,
                        LastName TEXT NOT NULL,
                        PhoneNumber TEXT NOT NULL,
                        Vacations TEXT NOT NULL,
                        Salary TEXT NOT NULL
                            );
                            """)
            connection1.commit()

            cursor1.execute("SELECT * FROM Workers")
            rows = cursor1.fetchall()

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(5)
            self.table_widget.setHorizontalHeaderLabels(
                ["First Name", "Last Name", "Phone Number","Vacations","Salary"])

            self.table_widget.setColumnWidth(0, 150)  # fname
            self.table_widget.setColumnWidth(1, 150)  # lname
            self.table_widget.setColumnWidth(2, 200)  # Pnmber
            self.table_widget.setColumnWidth(3, 150)  # vacations
            self.table_widget.setColumnWidth(4, 150)  # salary

            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

                connection1.commit()
        except Exception as e:
            print("Database error: " + str(e))
        finally:
            connection1.close()



class RegularCustomers(QMainWindow):
    def __init__(self):
        super(RegularCustomers, self).__init__()
        loadUi("customers_window.ui", self)

        self.setWindowTitle("Workers-Factors")
        self.setGeometry(100, 100, 650, 450)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.load_customers()

    def load_customers(self):
        try:
            connection1 = sqlite3.connect("Storage_Managment_Data.db")
            cursor1 = connection1.cursor()

            cursor1.execute("""CREATE TABLE IF NOT EXISTS Customers(
                        FirstName TEXT NOT NULL,
                        LastName TEXT NOT NULL,
                        PhoneNumber TEXT NOT NULL,
                        Purchases TEXT NOT NULL
                            );
                            """)
            connection1.commit()

            cursor1.execute("SELECT * FROM Customers")
            rows = cursor1.fetchall()

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(4)
            self.table_widget.setHorizontalHeaderLabels(
                ["First Name", "Last Name", "Phone Number","Purchases"])

            self.table_widget.setColumnWidth(0, 150)  # fname
            self.table_widget.setColumnWidth(1, 150)  # lname
            self.table_widget.setColumnWidth(2, 200)  # Pnmber
            self.table_widget.setColumnWidth(3, 150)  # Purchases

            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

                connection1.commit()
        except Exception as e:
            print("Database error: " + str(e))
        finally:
            connection1.close()







app = QApplication(sys.argv)
widget = QStackedWidget()
allapp = ButtonsScreen()
widget.addWidget(allapp)
widget.setFixedHeight(450)
widget.setFixedWidth(550)
widget.show()

try:
    sys.exit(app.exec())
except Exception as e:
    print(f"Exiting: {e}")
