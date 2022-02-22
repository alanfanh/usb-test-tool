#!/usr/bin/env python
#coding=utf-8
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from gui.gui import *
from core.USBStabilityTest import FtpTest,SmbTest
from time import sleep 

class RunThread(QtCore.QThread):

    OutSign = QtCore.Signal(str)
    Flag = QtCore.Signal(int)

    def __init__(self, parent=None):  
        super(RunThread,self).__init__(parent)
    
    def recv(self,ip,user,passwd,filename,remotopath,direction,serType,times):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.filename = filename
        self.remotopath = remotopath
        self.direction = direction
        self.serType = serType
        self.times = times
            
    def ftpUpload(self,ip,user,passwd,filename,remotopath):
        ftpclient=FtpTest(ip,user,passwd,filename,remotopath)
        ftp = ftpclient.connect()
        ftpclient._cwd(ftp) 
        ftpclient.Upload(ftp)
        sleep(3)
        ftpclient.delete(ftp)
        ftpclient.closeconnect(ftp)
        
    def ftpDownload(self,ip,user,passwd,filename,remotopath):
        ftpclient = FtpTest(ip,user,passwd,filename,remotopath)
        ftp = ftpclient.connect()
        ftpclient._cwd(ftp) 
        ftpclient.Download(ftp)
        sleep(3)
        ftpclient.closeconnect(ftp)
    
    def smbUpload(self,ip,user,passwd,filename,remotopath):
        smbclient = SmbTest(ip,user,passwd,filename,remotopath) 
        smbclient.connect()
        #print smbclient.list()
        smbclient.upload()
        #print smbclient.list()
        smbclient.delete()
    
    def smbDownload(self,ip,user,passwd,filename,remotopath):
        smbclient = SmbTest(ip,user,passwd,filename,remotopath) 
        smbclient.connect()
        #print smbclient.list()
        smbclient.download()
        #print smbclient.list()
    
    def run(self):
        self.function()
    
    def function(self):
        self.OutSign.emit(u"开始运行了！")
        sleep(2)
        for i in range(self.times):
            self.OutSign.emit(u"正在进行第%d次%s..." %((i+1),self.direction))
            sleep(1)
            print(i)
            if self.serType == "FTPSer":
                if self.direction == u"上传":
                    try:
                        self.ftpUpload(self.ip,self.user,self.passwd,self.filename,self.remotopath)
                    except:
                        self.OutSign.emit(u"第%d次上传失败" %(i+1))
                        self.Flag.emit(1)
                        sleep(2)     
                else :
                    try:
                        self.ftpDownload(self.ip,self.user,self.passwd,self.filename,self.remotopath)
                    except:
                        self.OutSign.emit(u"第%d次下载失败" %(i+1))
                        self.Flag.emit(1)
                        sleep(2)                        
                        
            if self.serType == "SambaSer":
                if self.direction == u"上传" :
                    try:
                        self.smbUpload(self.ip,self.user,self.passwd,self.filename,self.remotopath)
                    except:
                        self.OutSign.emit(u"第%d次上传失败" %(i+1))
                        self.Flag.emit(1)
                        sleep(2)                                                       
                else :
                    try:
                        self.smbDownload(self.ip,self.user,self.passwd,self.filename,self.remotopath)
                    except:
                        self.OutSign.emit(u"第%d次下载失败" %(i+1))
                        self.Flag.emit(1)
                        sleep(2)                                                
            self.OutSign.emit(u"已经完成第%d次%s！" %((i+1),self.direction))
            if (i+1)==self.times:
                self.OutSign.emit(u"所有%s成功，%s结束！" %(self.direction,self.direction))
            sleep(1)
            
            
            
class MainUi(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.m_ui =Ui_USBtest()
        self.m_ui.setupUi(self)
        self.thread = RunThread(self)
        self.m_ui.run.clicked.connect(self.main)
        self.m_ui.stop.clicked.connect(self.stopCopy)

    def main(self):
        self.flag = 0
        ip = str(self.m_ui.ftpip.toPlainText())
        user = str(self.m_ui.user.toPlainText())
        passwd = str(self.m_ui.passwd.toPlainText())
        filename = str(self.m_ui.filename.toPlainText())
        remotopath = str(self.m_ui.remotopath.toPlainText())
        direction = self.m_ui.direction.currentText()
        serType = self.m_ui.serType.currentText()
        times = int(self.m_ui.times.toPlainText())
        
        self.thread.recv(ip,user,passwd,filename,remotopath,direction,serType,times)
        self.thread.OutSign.connect(self.printStatus)
        self.thread.Flag.connect(self.setFlag)       
        self.thread.start()     
    
    def setFlag(self,t):
        self.stopCopy()
        self.flag = t 
        
    def stopCopy(self):
        if self.flag == 0:
            self.thread.terminate()
            self.thread.wait()          
        else:
            pass
        self.m_ui.status.append(u"已停止运行！")  
        
    def printStatus(self,str):
        self.m_ui.status.setText(str)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainUi = MainUi()
    MainUi.show()
    sys.exit(MainUi.exec())
    