from PySide2 import QtCore, QtGui
from PySide2.QtCore import ( QPropertyAnimation)
from PySide2.QtWidgets import *


WINDOW_SIZE = 0;

class UIFunctions:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow


    ########################################################################
    # Restore or maximize your window
    ########################################################################
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        
        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1 #Update value to show that the window has been maxmized
            self.mainwindow.showMaximized()

            # Update button icon  when window is maximized
            self.mainwindow.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/cil-window-restore.png"))#Show minized icon
        else:
        	# If the window is on its default size
            WINDOW_SIZE = 0 #Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.mainwindow.showNormal()

            # Update button icon when window is minimized
            self.mainwindow.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/cil-window-maximize.png"))#Show maximize icon
            

    # Start Menu buttons styling
    def applyButtonStyle(self):
        # Reset style for other buttons
        for w in self.mainwindow.ui.left_side_menu.findChildren(QPushButton):
            # If the button name is not equal to clicked button name
            if w.objectName() != self.mainwindow.sender().objectName():
                # Create default style by removing the left border
                # Lets remove the bottom border style
                defaultStyle = w.styleSheet().replace("border-bottom: 2px solid  rgb(0, 136, 255);", "")

                # Lets also remove the left border style
                defaultStyle = defaultStyle.replace("border-left: 2px solid  rgb(0, 136, 255);", "")

                # Apply the default style
                w.setStyleSheet(defaultStyle)
                        

        # Apply new style to clicked button
        # Sender = clicked button
        # Get the clicked button stylesheet then add new left-border style to it
        # Lets add the bottom border style
        newStyle = self.mainwindow.sender().styleSheet() + ("border-left: 2px solid  rgb(0, 136, 255);border-bottom: 2px solid  rgb(0, 136, 255);")
        # Apply the new style
        self.mainwindow.sender().setStyleSheet(newStyle)

    
    


    
    

        

    