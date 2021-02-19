import os
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import threading
import cv2
from PyQt5.QtCore import QCoreApplication, QThread
from subprocess import call
form_class = uic.loadUiType("gui.ui")[0]

# class Worker(QThread):
#     def run(self):
#         # os.system('python yolo.py')
#         fname = QFileDialog.getOpenFileName()

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
    
        super().__init__()
        self.setupUi(self)
        
        # self.work = Worker()

        
        
        self.gpspath = "/Users/pel-macmini2/gps/"
        self.slicepath = "/home/cvai2070/drone/ui_test"
        
        self.btn_1.clicked.connect(self.btn_videoslice)
        self.btn_2.clicked.connect(self.btn_yolo)
        self.btn_3.clicked.connect(self.btn_potholemap)
        self.btn_5.clicked.connect(self.btn_clear)
        self.btn_4.clicked.connect(QCoreApplication.instance().quit)

    def btn_videoslice(self):
        self.textBrowser_2.append("Slice Start")
        fname = QFileDialog.getOpenFileName(self)
        print(fname[0])

        vidcap = cv2.VideoCapture(fname[0])
        success,image = vidcap.read()
        
        count = 1
        success = True
        
        while success:
            cv2.imwrite("/home/cvai2070/drone/ui_test/%d.jpg" % count, image)
            success,image = vidcap.read()
            print("saved image %d.jpg" % count)
            
            count += 1
            
        self.textBrowser_2.append("Slice Finish")
            
        vidcap.release()
        
        
    def btn_yolo(self):
        self.textBrowser_2.append("YOLO start!!")
        time.sleep(1)
        os.system('python3 detect_result.py --source data/test.MP4 --weights drone_survivor.pt --classes 0 --project ui_test --img 3840')
        QApplication.processEvents()
        self.textBrowser_2.append("YOLO Finish!!")
        self.textBrowser_2.append("Go to /home/cvai2070/drone/ui_test")
        # self.work.start()
        fname = QFileDialog.getOpenFileName(self)
        
    
    def btn_potholemap(self):
        self.textBrowser_2.append("Mapping start!!")
        time.sleep(1)
        os.system('python3 matching.py')    # Shin Go
        self.textBrowser_2.append("Mapping file save!!")
        
        
    def btn_clear(self) :
        self.textBrowser_2.append("Data Clear Start")
        if os.path.isdir(self.gpspath):
            filelist1 = os.listdir(self.gpspath)
            for file in filelist1:
                os.remove(self.gpspath + file)
        else:
            self.textBrowser_2.append("GPS Folder not exist!")
        
        if os.path.isdir(self.slicepath):
            filelist2 = os.listdir(self.slicepath)
            for file in filelist2:
                os.remove(self.slicepath + file)
        else:
            self.textBrowser_2.append("Slice Folder not exist!")
        self.textBrowser_2.append("GPS and Slice Data clear")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()