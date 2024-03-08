chcp 65001
@echo off
:: 获取管理员权限
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrative permissions confirmed. Continuing...
) else (
    echo Requesting administrative privileges...
    powershell start -verb runas '%0'
    exit /b
)

:: 改成绝对目录
start pythonw "D:\workspace\chenyuan\py\project\mhxy_script\ui\mhxy_pyqt.py"