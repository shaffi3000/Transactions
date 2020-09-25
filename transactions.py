import sqlite3
import sys, os, time, uuid, hashlib, re
from PyQt5 import QtCore, QtGui, uic  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QComboBox, QTextEdit 

winMain = uic.loadUiType("transactions.ui") [0]

con = sqlite3.connect('banking_app.db')
cur = con.cursor()

class TestScreen(QtWidgets.QMainWindow, winMain): #imports the PyQT 'main window' functionality, winMain links to UI screens above

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored
        self.setupUi(self)
        self.searchBtn.clicked.connect(self.find)
        label = self.transOutLbl.setText(" ")

    def find(self):
        user1.getDetails()

        

class User():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def getDetails(self):
        cur.execute('SELECT merchant, debit, date FROM transactions')
        r = cur.fetchall()
        print(r)
        self.transactions(r)
        return (r)
            
    def transactions(self,r):
        items = []
        trans = []
        for i in range(len(r)):
            for x in r[i]:
                items.append(str(x))

        j = len(items)-1
        i = 0
        for x in range(0,j,3):
            print(i)
            trans.append([items[i], items[i+1], items[i+2]])
            i += 3

        text = []
        for x in range(0,len(trans)):
            val1 = trans[x][0]
            val2 = trans[x][1]
            val3 = trans[x][2]
            stringf = """ %s  %s  %s """ %(val1, val2, val3)
            text.append(stringf)
 
        winMain.transOutLbl.setText(text[0] + '\n' + text[1] )



user1 = User("Test",200)

app = QtWidgets.QApplication(sys.argv) #think of this as the 'main ()' section in procedural programming. Allows you to call the program into action 
winMain = TestScreen()

winMain.show()
app.exec_()




#items = []
#cur.execute('SELECT merchant, debit, date FROM transactions') 
#for row in cur:
    #items.append([row[0],row[1],row[2]])

#print(items)
