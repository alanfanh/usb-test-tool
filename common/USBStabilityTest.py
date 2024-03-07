#coding=utf-8
import sys
import ftplib
import socket
from smb.SMBConnection import SMBConnection

#FTP服务器
class FtpTest(object):

    #初始化
    def __init__(self,ip,user,passwd,filename,remotopath,BUFFER_SIZE = 8192):
        self.ip=ip
        self.user=user
        self.passwd=passwd
        self.filename=filename
        self.BUFFER_SIZE = BUFFER_SIZE 
        self.remotopath=remotopath
        if "\\" in self.filename:
            self.filename = self.filename.replace("\\","/")
        print(self.filename)
        if "/" in self.filename:
            self._filename = self.filename[self.filename.rindex("/")+1:]
        else:
            self._filename = self.filename
        print(self._filename)
    #连接ftp服务器
    def connect(self):
        try:
            print(self.ip)
            print(self.user)
            
            ftp = ftplib.FTP(self.ip,self.user,self.passwd)
            return ftp
        except socket.error or socket.gaierror: 
            print("create fail!")
            sys.exit(0)
            
    #进入远程目录
    def _cwd(self,ftp):
        ftp.cwd(self.remotopath)
    
    #当前目录下的文件列表
    def dir_list(self,ftp):
        ftp.dir()
    
    #下载文件
    def Download(self,ftp):
        try:
            f=open(self.filename,'wb').write
            ftp.retrbinary('RETR '+self._filename,f,self.BUFFER_SIZE)
            print("download suc!")
        except ftplib.error_perm:
            print("download fail!")
            sys.exit(0)
        
    #上传文件
    def Upload(self,ftp):
        try:
            f=open(self.filename,'rb')
            ftp.storbinary('STOR '+self._filename,f,self.BUFFER_SIZE)
            print("upload success!")
        except ftplib.error_perm:
            print("upload fail!")
            sys.exit(0)
            
    #删除文件
    def delete(self,ftp):
        ftp.delete(self._filename)
        print("delete success!")
            
    #关闭连接       
    def closeconnect(self,ftp):
        ftp.quit()
        
#Samba服务器       
class SmbTest(object):
    
    #初始化
    def __init__(self,ip,username,password,filename,remotopath):
        self.ip = ip
        self.username = username
        self.password = password
        self.filename=filename
        self.remotopath = remotopath
        if "\\" in self.filename:
            self.filename = self.filename.replace("\\","/")
        print(self.filename)
        if "/" in self.filename:
            self._filename = self.filename[self.filename.rindex("/")+1:]
        else:
            self._filename = self.filename
        print(self._filename)
        
    #连接samba服务器 
    def connect(self):
        self.server = SMBConnection(self.username,
                        self.password," "," ",use_ntlm_v2=True)
        self.server.connect(self.ip,139)
        print("connect success!")
        
    #上传文件
    def upload(self):
        data = open(self.filename,'rb')
        self._filename = '/' + self._filename   
        self.server.storeFile(self.remotopath,self._filename,data)
        print("file has been uploaded")
        data.close()
        
    #下载文件
    def download(self):
        fileobj = open(self.filename,'wb')
        self.server.retrieveFile(self.remotopath,self._filename,fileobj)
        print("file has been downloaded in current dir")
        fileobj.close()
    
    #删除文件
    def delete(self):
        print('remove file from remote share')
        self._filename = '/' + self._filename
        self.server.deleteFiles(self.remotopath,self._filename)
     
    
    #查看当前目录文件列表
    def list(self):
        print('list files of remote share')
        filelist = self.server.listPath(self.remotopath,'/')
        for f in filelist:
                print(f.filename)
    
