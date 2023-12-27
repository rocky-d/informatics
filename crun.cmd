@echo off
chcp 65001
setlocal enabledelayedexpansion

set "script_name=crun"

if ""=="%~1" (
    echo !script_name! ^>^> One parameter missing. :(
    exit /b 1
)

set "output_name=main"
set "output_dir=%~dp0\code\c\out"

for %%I in ("%~1") do cd "%%~dpI"
for %%i in ("%~1") do gcc "%%~nxi" -o "%output_dir%\!output_name!.exe"

if errorlevel 1 (
    echo !script_name! ^>^> Fail to compile. :(
    exit /b 1
)

"%output_dir%\%output_name%.exe"

endlocal
