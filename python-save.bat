@echo off

set "A=C:\Users\moon\Desktop\PythonAPI\Scripts"

cd "%A%"
REM 把目前的環境 匯出XX.txt
pip freeze > %~dp0requirements.txt 