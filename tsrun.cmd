@echo off

chcp 65001
cls

setlocal enabledelayedexpansion

set "script_name=tsrun"

if ""=="%~1" (
    echo %script_name% ^>^> One parameter missing. :(
    exit /b 1
)

set "output_name=out"
set "output_dir=%~dp0\code\ts\out"

for %%i in ("%~1") do (
    cd "%%~dpi"
    npx tsc "%%~nxi" --outFile "%output_dir%\%output_name%.js"
)

if errorlevel 1 (
    echo %script_name% ^>^> Fail to compile. :(
    exit /b 1
)

node "%output_dir%\%output_name%.js"

endlocal
