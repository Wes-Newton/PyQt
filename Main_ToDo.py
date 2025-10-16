# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 11:29:12 2025

@author: 220000177
"""

import json
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractListModel
from PyQt5.QtGui import QImage

from ToDo import Ui_MainToDo

basedir = os.path.dirname(__file__)
tick = QImage(os.path.join(basedir, 'tick.png'))

class TodoModel(QAbstractListModel):
    """
    
    
    """
    
    
    def __init__(self, todos = None):
        super().__init__()
        self.todos = todos or []
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        self.length = len(self.todos)
        return self.length


class MainTodo(QtWidgets.QMainWindow, Ui_MainToDo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('My ToDos')
        # todos = [(False, 'get nuts'), (False, 'get more nuts')]
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
        
    def load(self):
        try:
            with open('ToDoData.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass
    
    def save(self):
        with open('ToDoData.json', 'w') as f:
            # self.model.length_todos = len(self.model.todos)
            json.dump(self.model.todos, f)
            print('Saved!')
    
       
    
    def add(self):
        text = self.todoEdit.text()
        text = text.strip()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText('')
            self.save()
            
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()
                
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            self.save()
        
    
# app = QtWidgets.QApplication(sys.argv)
# window = MainTodo()
# window.show()
# app.exec_()

# https://doc.qt.io/qtforpython-6.5/PySide6/QtCore/QAbstractListModel.html#more












