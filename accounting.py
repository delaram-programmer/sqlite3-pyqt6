import sys
import sqlite3
from PyQt6.QtWidgets import *



class AccountingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accounting app")
        self.setGeometry(500, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("New transaction:")
        self.layout.addWidget(self.label)

        self.transaction_input = QLineEdit()
        self.layout.addWidget(self.transaction_input)

        self.add_button = QPushButton("Add transaction")
        self.add_button.clicked.connect(self.add_transaction)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete the transaction")
        self.delete_button.clicked.connect(self.delete_transaction)
        self.layout.addWidget(self.delete_button)

        self.transaction_list = QListWidget()
        self.layout.addWidget(self.transaction_list)

        self.setLayout(self.layout)

    def add_transaction(self):
        try :
           self.connection = sqlite3.connect("accounting.db")
           self.cursor = self.connection.cursor()
           self.connection.commit()
        except Exception as e:
            QMessageBox.critical(self,"Error" f"We are not connect to data base {str(e)}")

        transactionn = self.transaction_input.text()

        try:
            if transactionn:
                query = 'SELECT Id FROM transactions WHERE transaction = ?'
                self.cursor.execute(query, (transactionn,))
                self.cursor.execute('INSERT INTO transactions (transaction) VALUES (?)', (transaction,))
                self.connection.commit()
                self.transaction_input.clear()
                self.load_transactions()
            else:
                QMessageBox.warning(self, "Error", "Please add one transaction.")
        except Exception as e:
            QMessageBox.critical(self,"Error" f"We are not connect to data base {str(e)}")

    def delete_transaction(self):
        selected_item = self.transaction_list.currentItem()
        if selected_item:
            transaction_text = selected_item.text()
            self.cursor.execute('DELETE FROM transactions WHERE transaction = ?', (transaction_text,))
            self.connection.commit()
            self.load_transactions()
        else:
            QMessageBox.warning(self, "Error", "please choise one transaction.")

    def load_transactions(self):
        self.transaction_list.clear()
        self.cursor.execute('SELECT transaction FROM transactions')
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            self.transaction_list.addItem(transaction[0])



    def closeEvent(self, event):
        self.connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountingApp()
    window.show()
    sys.exit(app.exec())

# con = sqlite3.connect("accounting.db")
# cur = con.cursor()
# sqli = """
# SELECT * FROM transactions
# """
# acount = cur.execute(sqli)
# for row in acount:
#     print(row)
# con.commit()
# con.close()

