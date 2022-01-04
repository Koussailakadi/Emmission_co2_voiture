# -*- coding: utf-8 -*-

"""
Author: koussaila KADI 
        Salim Bedek
"""
import sys
import os


from PySide2 import QtCore
from PySide2.QtCore import ( QDateTime, Qt, QTimer)
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *



# Import user interface file
from ui_gui import *
import ui_functions 
from DataBase_manager import database


# Global value for the windows status
WINDOW_SIZE = 0;
# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #----attriburs:
        #================================== database ====================================
        self.database=database()
        self.params_con_server=dict()
        self.params_config_database=str
        self.marque=str
        self.modele_com=str
        self.designation_com=str
        self.cnit=str
        self.df_marque=None
        #=================================== Interfaces ============================== 
        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        
        #=================================== Butons ===================================
        self.ui_functions=ui_functions.UIFunctions(self)

        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.ui_functions.restore_or_maximize_window())
        

        #=================================les pages=====================================     
        #Set the page that will be visible by default when the app is opened 
        self.ui.stackedWidget.setCurrentWidget(self.ui.Connect_server)

        #navigate to Home page
        self.ui.connect_server.clicked.connect(self.getDataConnectServer)

        #navigate to Accounts page
        self.ui.cancel_server.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Connect_server))


        #navigate to fichier page
        self.ui.valid_config.clicked.connect(self.getDataConfigDatabase)

        #navigate to stats page
        self.ui.cancel_config.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Connectserver))


        #=================================les boutons:=====================================
        # combobox:
        self.marque=self.ui.comb_marque.currentIndexChanged.connect(self.getMarque_ui)
        self.modele_com=self.ui.comb_modele_com.currentIndexChanged.connect(self.getModele_com_ui)
        self.designation_com=self.ui.comb_designation_com.currentIndexChanged.connect(self.getDesignation_com_ui)
        self.designation_com=self.ui.search_cnit.clicked.connect(self.getCnit_ui)
        self.designation_com=self.ui.search_marque.clicked.connect(self.getDataSearch)
        
        #================================== mouve window with mouse=====================
        # Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size 
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
               
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.Title.mouseMoveEvent = moveWindow   

        

        # Show window
        self.show()



        # Add mouse events to the window
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    
    def getDataConnectServer(self):
        self.params_con_server={"user":self.ui.User.text(), "password":self.ui.Password.text(), "host":self.ui.Host.text()}
        print(self.params_con_server)
        self.database.connect(**self.params_con_server)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Database_config)

    def getDataConfigDatabase(self):
        params_config_database=self.ui.Database_name.text()
        print(params_config_database)
        isExistsDatabase=self.database.isExistsDataBase(params_config_database)

        if isExistsDatabase==0:
            self.database.createDatabase(params_config_database)
            self.database.getData(params_config_database,self.params_con_server)
            self.ui.stackedWidget.setCurrentWidget(self.ui.Connect_server)
            self.setup()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.database)
            self.database.useDataBase(params_config_database)
            self.setup()

    def getMarque_ui(self):
        self.marque=self.ui.comb_marque.currentText()

        df_modele_com=self.database.getMarque('Modele_com',condition=self.marque)
        for i in range(df_modele_com.shape[0]):
            self.ui.comb_modele_com.addItem("")
            self.ui.comb_modele_com.setItemText(i, QCoreApplication.translate('MainWindow', u""+df_modele_com.loc[i,'Modele_com'], None))
        
        # cas ou on clique pas sur le reste de combobox:
        self.designation_com=self.ui.comb_designation_com.currentText()
        self.modele_com=self.ui.comb_modele_com.currentText()

    
    def getModele_com_ui(self):
        self.modele_com=self.ui.comb_modele_com.currentText()
        df_designation_com=self.database.getMarque('Designation_com',condition=self.modele_com)
        for i in range(df_designation_com.shape[0]): 
            self.ui.comb_designation_com.addItem("")
            self.ui.comb_designation_com.setItemText(i, QCoreApplication.translate('MainWindow', u""+df_designation_com.loc[i,'Designation_com'], None))
    
    def getDesignation_com_ui(self):
        self.designation_com=self.ui.comb_designation_com.currentText()

    def getCnit_ui(self):
        self.cnit=self.ui.cnit.text()
        data_voiture=self.database.getDataFrameCnit(self.cnit)
        self.setTable(data_voiture)

    def getDataSearch(self):
        print(self.marque)
        print(self.modele_com)
        print(self.designation_com)
        self.df_marque=self.database.getDataFrameMaque("Marque",self.marque,self.modele_com, self.designation_com)
        self.setTable(self.df_marque)


    def setup(self):
        # add data to combobox marque:
        df_marque=self.database.getMarque('Marque',condition="")
        for i in range(df_marque.shape[0]):
            self.ui.comb_marque.addItem("")
            self.ui.comb_marque.setItemText(i, QCoreApplication.translate('MainWindow', u""+df_marque.loc[i,'Marque'], None))
            
        # set defaults values: 
        self.ui.comb_marque.setCurrentIndex(0) 
        self.ui.comb_modele_com.setCurrentIndex(0) 
        self.ui.comb_designation_com.setCurrentIndex(0) 

    
    def setTable(self,data):
        self.ui.tableWidget.setRowCount(data.shape[0])
        self.ui.tableWidget.setColumnCount(data.shape[1])
        print(data)
        horizontal_items={}
        for column in data.columns.to_list():
            print(column)
            horizontal_items["hor_items"+str(column)]=QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(column, horizontal_items["hor_items"+str(column)])
            
            #set items:
            horizontal_items["hor_items"+str(column)] = self.ui.tableWidget.horizontalHeaderItem(column)
            horizontal_items["hor_items"+str(column)].setText(QCoreApplication.translate("MainWindow", u""+str(column), None))
            """item=QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(item,column)
        
            #set items:
            items = self.ui.tableWidget.horizontalHeaderItem(column)
            items.setText(QCoreApplication.translate("MainWindow", u""+column, None))"""



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()    
    sys.exit(app.exec_())

 
        


    