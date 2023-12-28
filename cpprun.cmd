@echo off
chcp 65001
cls
setlocal enabledelayedexpansion

set "script_name=crun"

if ""=="%~1" (
    echo %script_name% ^>^> One parameter missing. :(
    exit /b 1
)

set "output_name=out"
set "output_dir=%~dp0\code\c\out"

for %%i in ("%~1") do (
    cd "%%~dpi"
    g++ "%%~nxi" -o "%output_dir%\%output_name%.exe"
)

if errorlevel 1 (
    echo %script_name% ^>^> Fail to compile. :(
    exit /b 1
)

"%output_dir%\%output_name%.exe"

endlocal
