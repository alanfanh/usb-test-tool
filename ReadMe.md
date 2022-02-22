# usb-test-tool

> PyQt project,the Test Tool of Router USB function module.

## 介绍

基于PySide6、pysmb、ftplib开发，测试路由器外接USB设备时Samba、FTP服务功能稳定性的带图形界面的测试工具。

### Developer

[FanHao](http://alanfanh.github)

### 项目结构

````text
usb-test-tool
|
|--common                # 工具项目的核心源码文件目录
|--gui                   # ui原文件,界面py文件
|
|--PyToExe.py            # py2exe打包配置文件
|--main.py               # 程序入口文件，启用界面主进程与工作子线程
|--ReadMe.md             # 本文件
````

## 环境

> python3.9.10 64bit

### 依赖

> 可使用"pip install -r requirements.txt"一键安装所有依赖项

````text
pyside6==6.2.3
pysmb==1.2.7
````