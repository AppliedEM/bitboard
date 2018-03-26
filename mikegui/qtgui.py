#!/usr/bin/python

#import mikesql
#from PyQt5.QtWidgets import (QWidget, QVboxLayout,QPushButton,QSizePolicy,QLabel,QApplication)
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton,QScrollArea, QLineEdit,
	QSizePolicy, QLabel, QTextEdit, QApplication)
from PyQt5.Qt import QApplication, QClipboard
#import PyQtkkj
import sys

class Window(QWidget):

	def __init__(self):
		super(Window,self).__init__()
		self.initUI()
	
	def initUI(self):
		grid = QGridLayout()
		grid.setSpacing(10)

		clearbtn = QPushButton('Clear Inputs',self)
		exitbtn = QPushButton('Close Window',self)
		sendbtn = QPushButton('Send',self)
		receivebtn = QPushButton('Receive',self)
		importbtn = QPushButton('Import',self)
		clearbtn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		clearbtn.move(20,20)

		amount_label = QLabel("Amount: ",self)
		address_label = QLabel("Address: ",self)
		fee_label = QLabel("Fee: ",self)
		import_label = QLabel("Import: ",self)
		updates = QLabel("Updates go here.",self)

		amount_input = QLineEdit('amount',self)
		address_input = QLineEdit('address',self)
		fee_input = QLineEdit('fee',self)
		import_input = QLineEdit('import',self)

		grid.addWidget(clearbtn,1,0)
		grid.addWidget(sendbtn,2,0)
		grid.addWidget(amount_label,2,1)
		grid.addWidget(amount_input,2,2)
		grid.addWidget(address_label,1,1)
		grid.addWidget(address_input,1,2)
		grid.addWidget(importbtn,4,0)
		grid.addWidget(import_input,4,2)
		grid.addWidget(import_label,4,1)
		grid.addWidget(receivebtn,3,0)
		grid.addWidget(fee_label,3,1)
		grid.addWidget(fee_input,3,2)
		grid.addWidget(exitbtn,5,0)
		grid.addWidget(updates,5,1,6,2)

		"""
		This begins the functions that will be bound to the buttons. The 'clear inputs' and exit buttons are already set up. The receive button has just some code to test the clipboard functionality
		"""
		def clear_textboxes():
			amount_input.setText("")
			fee_input.setText("")
			address_input.setText("")
			import_input.setText("")
			updates.setText("Input boxes have been cleared!")

		def send():
			pass

		def receive():
			useaddress = address_input.text()
			QApplication.clipboard().setText(useaddress)
			updates.setText("Address input field \"" + useaddress + "\" has been copied to the clipboard.")


		#Buttons are bound to a function here
		exitbtn.clicked.connect(quit)
		clearbtn.clicked.connect(clear_textboxes)
		receivebtn.clicked.connect(receive)

		self.setLayout(grid)
		self.setGeometry(300,300,1300,1000)
		self.setWindowTitle('SQL GU Interface')
		self.show()
	"""
	def active_projects(self):
		#active = mikesql.runquery("Select * from warehouse.project where active is true;",True)
		#print str(active)
		output = ''
		for line in active:
			output+=str(line) + '\n'
		#self.lbl.setWordWrap(True)
		#self.lbl.setText(output)
		#print self.lbl.textFormat()
	"""

print("Hello")
if __name__ == "__main__":

	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())
