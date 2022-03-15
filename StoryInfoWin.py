# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:03:25 2020

@author: ibrahim
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'story_info_input_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Story_info_screen(object):
    def setupUi(self, Story_info_screen):
        Story_info_screen.setObjectName("Story_info_screen")
        Story_info_screen.resize(531, 386)
        self.groupBox = QtWidgets.QGroupBox(Story_info_screen)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 281))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 20, 191, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.story_heights = QtWidgets.QTableWidget(self.groupBox_2)
        self.story_heights.setGeometry(QtCore.QRect(10, 20, 171, 221))
        self.story_heights.setShowGrid(True)
        self.story_heights.setRowCount(1)
        self.story_heights.setColumnCount(1)
        self.story_heights.setObjectName("story_heights")
        item = QtWidgets.QTableWidgetItem()
        self.story_heights.setItem(0, 0, item)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 20, 191, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.story_weights = QtWidgets.QTableWidget(self.groupBox_3)
        self.story_weights.setGeometry(QtCore.QRect(0, 20, 171, 221))
        self.story_weights.setRowCount(1)
        self.story_weights.setColumnCount(1)
        self.story_weights.setObjectName("story_weights")
        item = QtWidgets.QTableWidgetItem()
        self.story_weights.setItem(0, 0, item)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 51, 251))
        self.groupBox_4.setObjectName("groupBox_4")
        self.story_info_save_button = QtWidgets.QPushButton(Story_info_screen)
        self.story_info_save_button.setGeometry(QtCore.QRect(380, 300, 93, 28))
        self.story_info_save_button.setObjectName("story_info_save_button")

        self.retranslateUi(Story_info_screen)
        QtCore.QMetaObject.connectSlotsByName(Story_info_screen)

    def retranslateUi(self, Story_info_screen):
        _translate = QtCore.QCoreApplication.translate
        Story_info_screen.setWindowTitle(_translate("Story_info_screen", "Kat Bilgileri"))
        self.groupBox.setTitle(_translate("Story_info_screen", "Kat Bilgileri"))
        self.groupBox_2.setTitle(_translate("Story_info_screen", "Kat Yükseklikleri (m)"))
        __sortingEnabled = self.story_heights.isSortingEnabled()
        self.story_heights.setSortingEnabled(False)
        item = self.story_heights.item(0, 0)
        item.setText(_translate("Story_info_screen", "0"))
        self.story_heights.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Story_info_screen", "Kat Kütleleri (ton)"))
        __sortingEnabled = self.story_weights.isSortingEnabled()
        self.story_weights.setSortingEnabled(False)
        item = self.story_weights.item(0, 0)
        item.setText(_translate("Story_info_screen", "0"))
        self.story_weights.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("Story_info_screen", "Kat"))
        self.story_info_save_button.setText(_translate("Story_info_screen", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Story_info_screen = QtWidgets.QWidget()
    ui = Ui_Story_info_screen()
    ui.setupUi(Story_info_screen)
    Story_info_screen.show()
    sys.exit(app.exec_())