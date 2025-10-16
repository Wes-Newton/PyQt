# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 16:27:35 2025

@author: 220000177
"""

import sys
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QDial,
                            QSizePolicy, QMessageBox)

class _Bar(QWidget):
    
    def __init__(self, steps):
        super().__init__()
        self.setting = 0
        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding,
            )
        
        if isinstance(steps, list):
            self.n_steps = len(steps)
            self.steps = steps
    
        elif isinstance(steps, int):
            self.n_steps = steps
            self.steps = ['red'] * steps
            
        else:
            raise TypeError('steps must be a list or int')
            
        self._bar_solid_percent = 0.8
        self._background_color = QColor('black')
        self._padding = 1
    
    def sizeHint(self):
        return QSize(40,120)
    
    def paintEvent(self, e):
        painter = QPainter(self)
        
        brush = QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0,
                    0,
                    painter.device().width(),
                    painter.device().height(),
                    )
        painter.fillRect(rect, brush)
        
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()
 
        d_height = painter.device().height() - (self._padding *2)
        d_width = painter.device().width() - (self._padding * 2)
 
        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent
        
        pc = (value - vmin) / (vmax - vmin)
        n_boxes = int(pc * self.n_steps)
        self.setting = n_boxes
    
        for n in range(n_boxes):
            brush.setColor(QColor(self.steps[n]))
            ypos = (1 + n) * step_size
            rect = QRect(
                    self._padding,
                    self._padding + d_height - int(ypos),
                    d_width,
                    int(bar_height),
                    )
            painter.fillRect(rect, brush)
        painter.end()
        

    def _trigger_refresh(self):
        
        self.update()

class PowerBar(QWidget):

    def __init__(self, parent=None, steps = 5):
        super().__init__(parent)
        layout = QVBoxLayout()
        self._bar = _Bar(steps)
        
        layout.addWidget(self._bar)
        
        self._dial = QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setWrapping(False)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)
        
        self.setLayout(layout)
    
    def closeEvent(self, e):
        mesgOk = QMessageBox()
        mesgOk.setStandardButtons(QMessageBox.Ok)
        mesgOk.setIcon(QMessageBox.Information)
        mesgOk.setWindowTitle('Pop-Up on Close')
        message = 'Your Setting Is ' + str(self._bar.setting)
        mesgOk.setText(message)
        mesgOk.exec_()
        
