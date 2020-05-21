@echo off
REM && chcp 65001
REM #############
REM if not  defined top (call top)
REM echo.%top%
REM set  TT=%top%
REM #############

REM rem 會自動產生..相對的目錄
REM set WORKON_HOME=%~dp0Envs
REM workon


set A=%1
set B=%2


rem 會自動產生..相對的目錄
set WORKON_HOME=%~dp0Envs
REM 如果登入..不存在 top 禁止動作
IF EXIST %~dp0\Envs\ok.vm  (
    REM 強制登出
    if "%B%"=="D" (
        if "%A%"=="exit" (
        REM #####################
        REM set "XX="
        REM set /p XX=<%~dp0Envs\ok.vm
        REM REM 中間要輸出 不然會影響 top
        REM echo.%XX%
        REM set top=%XX:~0,-1%
        REM echo.%top%
        REM cd    %~dp0Envs\%top%
        REM del   login.vm
        dirFOR
        cd    %~dp0Envs
        del   ok.vm
        set "XX="
        set "top="
        set "A="
        set "B="
        goto _end 
        )
    )
    REM if "%B%"=="L"  ( 
    REM     C:\Users\moon\Desktop\PyVM\bin\Envs\%A%\Scripts\activate 
        
    REM     REM BAT 是執行整個區塊 goto 不是跳出...指定 區塊結束的出口
    REM     goto _end 
    REM ) else (
        if not defined top ( 
            echo.Please log out !!
            echo.
            goto _end 
        )
    REM )
)

rem if defined A (mkvirtualenv %A%) else (echo.請填入名稱)
if defined A (
if defined B (
    REM 退出 (強制) ...不建議 !! 會少刪檔案
    REM if "%A%"=="exit" (
    REM     if "%B%"=="D"  (
    REM         del %~dp0\Envs\ok.vm
    REM         call %~dp0
    REM     )
    REM )
    REM 改用手動刪除吧..如果關閉CMD..刪除 ok.vm
    if "%B%"=="D"  (
        REM 如果再登入..不可以刪除
        IF not EXIST %~dp0\Envs\ok.vm  (        
            rmvirtualenv %A%
        ) else (
            echo.Please log out !!
            echo.
        )
    )
    REM if "%B%"=="H"  ( cls & cdvirtualenv )
    REM if "%A%"=="S"  ( cls & cdsitepackages )
    
) else (
REM 這邊是 只有A沒有B

    REM 登入
    IF EXIST %~dp0\Envs\%A% (
        
        REM 拷貝,自動登出
        IF EXIST %~dp0\Envs\ok.vm  (
            REM #####################
            set "XX="
            set /p XX=<%~dp0Envs\ok.vm
            set top=%XX:~0,-1%
            if not "%top%" == "%A%" ( 
                REM 登出
                deactivate 
                REM 登出的憑證(唯一)
                del %~dp0\Envs\%top%\login.vm
                del %~dp0\Envs\ok.vm
                set "top="
                set "XX="
                set topB=%top%
                REM 不相同就登出...再登入帳號
                call %~dpxn0 exit
                REM echo.################################################### not login!!  
                REM goto _end     
            )
        )
 

        
        REM 因為要登入,所以一律初始化,重新設定
        set "top="
        %~dp0Envs\%A%\Scripts\activate
        REM 更新 top 變數 
        REM 回到 Hone  
        cdvirtualenv
        REM 取得上層
        if not  defined top (call top)
        REM 完成登入
        echo.ok>login.vm 
        cd %~dp0\Envs
        echo.%A%>ok.vm 
        cdvirtualenv


        
 
    
        
    ) ELSE (
        

        REM 退出
        if "%A%"=="exit" (
            
            REM 正在 登入狀態
            IF EXIST %~dp0\Envs\ok.vm  (
                set "XX="
                set /p XX=<%~dp0Envs\ok.vm
                set top=%XX:~0,-1%
                REM 登出
                deactivate 
                REM 登出的憑證(唯一)
                del %~dp0\Envs\%top%\login.vm
                del %~dp0\Envs\ok.vm
                set "top="
                set "XX="
                %~dpxn0 
            )
            
           
        ) else (
            if "%A%"=="H" (  
                REM 正在 登入狀態
                IF EXIST %~dp0\Envs\ok.vm  (
                    set "XX="
                    set /p XX=<%~dp0Envs\ok.vm
                    set top=%XX:~0,-1%
                    REM 登出
                    %~dp0\Envs\%top%\Scripts\activate
                    cdvirtualenv
                )
            ) else (
                if "%A%"=="S"  ( 
                            REM 正在 登入狀態
                            IF EXIST %~dp0Envs\ok.vm  (
                                set "XX="
                                set /p XX=<%~dp0Envs\ok.vm
                                set top=%XX:~0,-1%
                                REM 登出
                                %~dp0Envs\%top%\Scripts\activate
                                cdvirtualenv
                                REM 檢查檔案
                                REM 存檔
                                echo.
                                type  %~dp0Envs\%top%\requirements.txt 
                                pip freeze > requirements.txt 
                                echo.
                                echo.^(%top%^) SAVE !!
                                echo.

                            )
                ) else (
                            if "%A%"=="IN"  ( 
                                REM 正在 登入狀態
                                IF EXIST %~dp0Envs\ok.vm  (
                                    set "XX="
                                    set /p XX=<%~dp0Envs\ok.vm
                                    set top=%XX:~0,-1%
                                    REM 登出
                                    %~dp0Envs\%top%\Scripts\activate
                                    cdvirtualenv
                                    REM 檢查檔案
                                    IF EXIST %~dp0Envs\%top%\requirements.txt  (
                                        REM 安裝
                                        pip install -r requirements.txt
                                        cls
                                        echo.
                                        echo.^(%top%^) ######################### SETUP !! ##########################
                                        echo.
                                    ) else ( 
                                        pip freeze > requirements.txt 
                                    )
                                )
                            ) else (
                                REM 拷貝,自動登出
                                IF EXIST %~dp0\Envs\ok.vm  (
                                    REM #####################
                                    set "XX="
                                    set /p XX=<%~dp0Envs\ok.vm
                                    set top=%XX:~0,-1%
                                    if not "%top%" == "%A%" ( 
                                        REM 登出
                                        deactivate 
                                        REM 登出的憑證(唯一)
                                        del %~dp0\Envs\%top%\login.vm
                                        del %~dp0\Envs\ok.vm
                                        set "top="
                                        set "XX="
                                        set topB=%top%
                                        REM 不相同就登出...再登入帳號
                                        call %~dpxn0 exit
                                        REM echo.################################################### not login!!  
                                        REM goto _end     
                                    )
                                )

                                REM 因為要登入,所以一律初始化,重新設定
                                set "top="
                                mkvirtualenv %A%  > log.txt
                                del log.txt

                                REM 更新 top 變數 
                                REM 回到 Hone  
                                cdvirtualenv
                                REM 取得上層
                                if not  defined top (call top)
                                REM 完成登入
                                echo.ok>login.vm 
                                cd %~dp0\Envs
                                echo.%A%>ok.vm 
                                cdvirtualenv

                            )
                )
            )
        ) 
    
       
    )
   
)
) else (workon)



REM ### 注意 只能處理一個 VM
REM ### 如果



:_end
