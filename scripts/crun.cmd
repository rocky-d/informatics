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
set "output_dir=%~dp0code\c\out"

for %%i in ("%~1") do (
    cd "%%~dpi"
    gcc -o "%output_dir%\%output_name%.exe" "%%~nxi"
    "%output_dir%\%output_name%.exe"
)

endlocal
