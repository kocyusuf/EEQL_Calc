# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:27:31 2020

@author: yusufkoc
"""
import EQLoS as eql
import StoryInfoWin as siw
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        # self.win = None
        self.ui = eql.Ui_Form()
        self.ui.setupUi(self) 
        self.ui.draw_graphic.clicked.connect(self.spectrumGraphics)
        self.ui.story_info_button.clicked.connect(self.storyInfoWin)
        self.ui.calculate_button.clicked.connect(self.calcLoads)
    
    def storyInfoWin(self):
        self.win = QtWidgets.QMainWindow()
        self.story_win = siw.Ui_Story_info_screen()
        self.story_win.setupUi(self.win)
        self.win.show()
        self.number_story = int(self.ui.number_stories.text())
        self.story_win.story_heights.setHorizontalHeaderLabels(["Kat Yüksekliği"])
        self.story_win.story_weights.setHorizontalHeaderLabels(["Kat Ağırlığı"])
        self.story_win.story_heights.setRowCount(self.number_story)
        self.story_win.story_weights.setRowCount(self.number_story)
        self.story_win.story_info_save_button.clicked.connect(self.takeInfo)
        
    def takeInfo(self):
        self.storyWeights = []
        self.storyHeights = []
        self.sum_storyWeights = []
        self.sum_storyHeights = []
        for weight in range(self.number_story):
            self.storyWeights.append(float(self.story_win.story_weights.item(weight,0).text()))
            self.storyHeights.append(float(self.story_win.story_heights.item(weight,0).text()))
            self.sum_storyWeights.append(sum(self.storyWeights))
            self.sum_storyHeights.append(sum(self.storyHeights))
        self.ui.sum_structure_weight.setText(str(self.sum_storyWeights[-1]))
        self.ui.sum_structure_height.setText(str(self.sum_storyHeights[-1]))
        
    def spectrumGraphics(self):
        self.short_period_spectral_coeff = float(self.ui.short_period_spectral.text())
        self.one_second_period_spectral_coeff = float(self.ui.one_second_period_spectral.text())

        self.periods_graphics = np.arange(0,10,0.01)
        self.corner_period_big_result = round(self.one_second_period_spectral_coeff / self.short_period_spectral_coeff,4)
        self.corner_period_small_result = round(self.corner_period_big_result * 0.20,4)
        self.long_period = 6.0
        self.ui.corner_period_small_spectral.setText(str(self.corner_period_small_result))
        self.ui.corner_peiod_big_spectral.setText(str(self.corner_period_big_result))
        
        self.spectrum = []
        self.periods = []
        for self.period in self.periods_graphics:
            if 0 <= self.period < self.corner_period_small_result:
                self.Sae = (0.4 + 0.6 * self.period / self.corner_period_small_result) * self.short_period_spectral_coeff
                self.spectrum.append(self.Sae)
                self.periods.append(self.period)

            elif self.corner_period_small_result <= self.period <= self.corner_period_big_result:
                self.Sae = self.short_period_spectral_coeff
                self.spectrum.append(self.Sae)
                self.periods.append(self.period)

            elif self.corner_period_big_result < self.period <= self.long_period:
                self.Sae = self.one_second_period_spectral_coeff / self.period
                self.spectrum.append(self.Sae)
                self.periods.append(self.period)

            else:
                self.Sae = self.one_second_period_spectral_coeff * self.long_period / (self.period ** 2)
                self.spectrum.append(self.Sae)
                self.periods.append(self.period)
        
        plt.plot(self.periods, self.spectrum, "blue")
        plt.xlabel("Periyot")
        plt.ylabel("Yatay elastik tasarım spektral ivmesi")
        #plt.savefig("spektralGraph.png")
        #self.graphic.show()
        #self.imageGraph = QtGui.QImage("spektralGraph.png")
        #self.sizeImage =self.imageGraph(QtCore.QSize(100,100))
        #self.palette = QtGui.QPalette()
        #self.palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(self.sizeImage))
        #self.setPalette(self.palette)
    
    def calcLoads(self):
        self.ui.list_X.clear()
        self.ui.list_Y.clear()
        self.period_structure_X = float(self.ui.period_structure_X_direct.text())
        self.period_structure_Y = float(self.ui.period_structure_Y_direct.text())
        self.eql_reduce_coeff_X = int(self.ui.EQL_reduce_coeff_X_direct.text())
        self.eql_reduce_coeff_Y = int(self.ui.EQL_reduce_coeff_Y_direct.text())
        self.important_coeff = float(self.ui.struct_important_coeff.text())
        
        if 0 <= self.period_structure_X <= self.corner_period_small_result:
            self.Sae_X = (0.4 + 0.6 * (self.period_structure_X / self.corner_period_small_result)) * self.short_period_spectral_coeff
        elif self.corner_period_small_result <= self.period_structure_X <= self.corner_period_big_result:
            self.Sae_X = self.short_period_spectral_coeff
        elif self.corner_period_big_result <= self.period_structure_X <= self.long_period:
            self.Sae_X = self.one_second_period_spectral_coeff / self.period_structure_X
        else:
            self.Sae_X = (self.one_second_period_spectral_coeff * self.long_period) / (self.period_structure_X ** 2)

        if 0 <= self.period_structure_Y <= self.corner_period_small_result:
            self.Sae_Y = (0.4 + 0.6 * (self.period_structure_Y / self.corner_period_small_result)) * self.short_period_spectral_coeff
        elif self.corner_period_small_result <= self.period_structure_Y <= self.corner_period_big_result:
            self.Sae_Y = self.short_period_spectral_coeff
        elif self.corner_period_big_result <= self.period_structure_Y <= self.long_period:
            self.Sae_Y = self.one_second_period_spectral_coeff / self.period_structure_Y
        else:
            self.Sae_Y = (self.one_second_period_spectral_coeff * self.long_period) / (self.period_structure_Y ** 2)
        
        self.SaR_X = self.Sae_X / self.eql_reduce_coeff_X
        self.SaR_Y = self.Sae_Y / self.eql_reduce_coeff_Y
        self.Vt_X = round((float(self.ui.sum_structure_weight.text()) * self.SaR_X * 9.8075),3)
        self.Vt_Y = round((float(self.ui.sum_structure_weight.text()) * self.SaR_Y * 9.8075),3)
        
        self.ui.base_shear_load_X_direct.setText(str(self.Vt_X))
        self.ui.base_shear_load_Y_direct.setText(str(self.Vt_Y))
        
        self.loadFile = open("storyloads_new.txt","w")
        self.StoryLoad_X = []
        self.StoryLoad_Y = []
        
        self.deltaFN_X = 0.0075 * int(self.ui.number_stories.text()) * self.Vt_X
        self.deltaFN_Y = 0.0075 * int(self.ui.number_stories.text()) * self.Vt_Y
        self.sum_Fi_X = self.Vt_X - self.deltaFN_X
        self.sum_Fi_Y = self.Vt_Y - self.deltaFN_Y
        
        self.miHi = [a * b for a,b in zip(self.storyWeights, self.sum_storyHeights)]
        self.sum_miHi = sum(self.miHi)
        for self.mHx in self.miHi:
            self.Fi_X = self.sum_Fi_X * (self.mHx / self.sum_miHi)
            self.StoryLoad_X.append(self.Fi_X)
        for self.mHy in self.miHi:
            self.Fi_Y = self.sum_Fi_Y * (self.mHy / self.sum_miHi)
            self.StoryLoad_Y.append(self.Fi_Y)
            
        i = 0
        while i < int(self.ui.number_stories.text()): 
            self.result_text_X = f"{i+1}. kata etkiyen deprem yükü X : {round((self.StoryLoad_X[i]),2)}"
            self.result_text_Y = f"{i+1}. kata etkiyen deprem yükü Y : {round((self.StoryLoad_Y[i]),2)}"
            self.ui.list_X.addItem(self.result_text_X)
            self.ui.list_Y.addItem(self.result_text_Y)
            i += 1
        
        

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.setWindowIcon(QtGui.QIcon("icon.jpg"))
    win.show()
    sys.exit(app.exec_())
    
app()