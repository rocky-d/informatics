@echo off
chcp 65001
setlocal enabledelayedexpansion

set "script_name=crun"

if ""=="%~1" (
    echo !script_name! ^>^> One parameter missing. :(
    exit /b 1
)

for %%I in ("%~1") do set "PATH=%PATH%;%%~dpI"
echo %PATH%

rem Get file name (without suffix)
rem for %%i in ("%~1") do set "output_name=%%~ni"
set "output_name=main"

set "output_dir=.\code\c\out"

gcc "%~1" -o "%output_dir%\!output_name!.exe"

if errorlevel 1 (
    echo !script_name! ^>^> Fail to compile. :(
    exit /b 1
)

"%output_dir%\!output_name!.exe"

endlocal
