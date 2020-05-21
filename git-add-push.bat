@echo off
REM YES
git config --global https.proxy 'socks5://127.0.0.1:1080'
git config --global http.proxy  'socks5://127.0.0.1:1080'
REM 儲存目前的分支
call name-B





IF "%3"=="" (goto _A) else ( set "C03=%1 %2 %3"&goto _C)

:_A
IF "%2"=="" (goto _B) else ( set "C03=%1 %2"&goto _C)

:_B
IF "%1"=="" (echo.) else ( set "C03=%1"&goto _C) 

:_C

git add --all
git commit -m "%C03%"
REM #明確指定 ######################################
REM git push #######################################
call top
if "top"=="no-0"  ( echo.dirPath? & goto _end )
git push %top%  %name-B%:%name-B%
REM ################################################








REM NO
git config --global --unset https.proxy
git config --global --unset http.proxy