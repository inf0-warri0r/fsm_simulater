#!/usr/bin/env python

"""
Author : tharindra galahena (inf0_warri0r)
Project: fsm simulater
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 03/06/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

"""
test case :
-------------

floatnumber=pointfloat|exponentfloat
exponentfloat=(intpart|pointfloat)exponent
pointfloat=[intpart]fraction|intpart(.)
fraction=.((digit)+)
exponent=(e|E)[_+|-]((digit)+)
intpart=(digit)+
digit=0|1|2|3|4|5|6|7|8|9

"""

from PySide import QtGui, QtCore
from fsm_ui import Ui_MainWindow
import sys
import make_list
import fsm


class MyWidget(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.main_fsm = ""
        self.rd = make_list.read_lt()
        self.fsms = {}
        self.current_state = ''
        self.current_string = ''
        self.generate.clicked.connect(self.generate_fsm)
        self.test.clicked.connect(self.test_fsm)
        self.go.clicked.connect(self.go_fsm)
        self.reset.clicked.connect(self.reset_fsm)
        self.definitions.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 500, 500)
        self.state_view.setScene(self.scene)
        self.pen_b = QtGui.QPen(QtCore.Qt.blue, 1, QtCore.Qt.SolidLine)
        self.pen_r = QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        self.pen_y = QtGui.QPen(QtCore.Qt.yellow, 1, QtCore.Qt.SolidLine)

    def draw_state(self):
        self.scene.clear()
        lst = {}
        if self.current_state in self.fsms[self.main_fsm].table:
            m = self.fsms[self.main_fsm].table[self.current_state]
            for key in m.keys():
                if m[key] in lst:
                    lst[m[key]] = lst[m[key]] + "," + key
                else:
                    lst[m[key]] = key

        l = len(lst.keys())
        keys = lst.keys()
        mp = 250 - 60 * (l - 1) / 2
        fs = self.fsms[self.main_fsm].end_states
        self.scene.addEllipse(100, mp, 35, 35, self.pen_r)
        if self.current_state in fs:
            self.scene.addEllipse(103, mp + 3, 29, 29, self.pen_r)
        stat = self.fsms[self.main_fsm].states[self.current_state]
        item = QtGui.QGraphicsTextItem(stat)
        item.setPos(105, mp + 5)
        self.scene.addItem(item)
        if l > 0:
            for i in range(0, len(keys)):
                p = 250 - l * 60 / 2 + 60 * i
                self.scene.addEllipse(300, p, 35, 35, self.pen_b)
                if keys[i] in fs:
                    self.scene.addEllipse(303, p + 3, 29, 29, self.pen_b)
                self.scene.addLine(135, mp + 15, 300, p + 15, self.pen_y)
                item = QtGui.QGraphicsTextItem(lst[keys[i]])
                item.setPos(215 - item.boundingRect().width() / 2,
                            (mp + p) / 2 - 5)
                self.scene.addItem(item)
                stat = self.fsms[self.main_fsm].states[keys[i]]
                item = QtGui.QGraphicsTextItem(stat)
                item.setPos(305, p + 5)
                self.scene.addItem(item)

    def generate_fsm(self):
        self.current_string = ""
        self.fsm = {}
        doc = self.definitions.document()
        block = doc.begin()
        lits = list()
        if block.text() != '':
            s = block.text().split('=')
            if len(s) == 2:
                lits.append(s)
        for i in range(1, doc.blockCount()):
            block = block.next()
            if block.text() != '':
                s = block.text().split('=')
                if len(s) == 2:
                    lits.append(s)

        if len(lits) <= 0:
            return
        for i in range(0, len(lits)):
            ls = self.rd.tree_list(('', lits[i][1]))
            self.fsms[lits[i][0]] = fsm.fsm([], [], str(i))
            self.fsms[lits[i][0]].chain2(str(i) + '0', str(i) + '1',
                                        str(i), ls, i)
            self.print_fsm_table(self.fsms[lits[i][0]])

        s = list()
        for i in range(len(lits) - 1, -1, -1):
            s.append(lits[i])

        for i in range(0, len(s)):
            for j in range(0, i):
                print "------------------------------------------", i
                self.fsms[s[i][0]].join(self.fsms[s[j][0]], s[j][0])
                #self.fsms[s[i][0]].add()

        self.main_fsm = lits[0][0]
        self.fsms[self.main_fsm ].add()
        self.fsms[self.main_fsm].map_states()
        self.print_fsm_table(self.fsms[self.main_fsm])
        self.current_state = self.fsms[self.main_fsm].start_states[0]
        st = self.fsms[self.main_fsm].states[self.current_state]
        self.current_st.setText(st)
        self.draw_state()

    def print_fsm_table(self, f):
        for k in f.table.keys():
            s = k + " -"
            for l in f.table[k].keys():
                s = s + " " + l + ":" + f.table[k][l]

            print s

        print "end-states"
        for s in f.end_states:
            print s
        print "start-states"
        for s in f.start_states:
            print s
        print "------------------------\n"

    def test_fsm(self):
        if self.main_fsm not in self.fsms:
            QtGui.QMessageBox.about(self, "ERROR", "generate a fsm first")
            return

        tst = self.test_string.text()
        if tst == '':
            return
        self.reset_fsm()
        self.current_state = self.fsms[self.main_fsm].start_states[0]

        f = True
        for i in range(0, len(tst)):
            if self.fsms[self.main_fsm].transfer(tst[i]):
                self.current_state = self.fsms[self.main_fsm].current_state
                self.current_string = self.current_string + tst[i]
            else:
                QtGui.QMessageBox.about(self, "ERROR",
                                        "cannot accept the string")
                self.draw_state()
                f = False
                break
        if f:
            if self.current_state in self.fsms[self.main_fsm].end_states:
                QtGui.QMessageBox.about(self, "SUCCESS", "String is accepted")
                self.draw_state()
            else:
                QtGui.QMessageBox.about(self, "ERROR",
                                        "cannot accept the string")
                self.draw_state()

    def go_fsm(self):
        if self.main_fsm not in self.fsms:
            QtGui.QMessageBox.about(self, "ERROR", "generate a fsm first")
            return
        tst = self.test_char.text()
        if tst == '':
            return

        if self.fsms[self.main_fsm].transfer(tst):
            self.current_state = self.fsms[self.main_fsm].current_state
            self.current_string = self.current_string + tst
            sta = self.fsms[self.main_fsm].states[self.current_state]
            self.current_st.setText(sta)
            self.current_str.setText(self.current_string)
            self.draw_state()
        else:
            QtGui.QMessageBox.about(self, "ERROR", "cannot accept the char")
            self.draw_state()

    def reset_fsm(self):
        self.current_string = ""
        self.fsms[self.main_fsm].reset()
        self.current_state = self.fsms[self.main_fsm].current_state
        s = self.fsms[self.main_fsm].states[self.current_state]
        self.current_st.setText(s)
        self.current_str.setText("")
        self.test_string.setText("")
        self.test_char.setText("")
        self.draw_state()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
