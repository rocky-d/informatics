@echo off

chcp 65001
cls

setlocal enabledelayedexpansion

set "script_name=rsrun"

if ""=="%~1" (
    echo %script_name% ^>^> One parameter missing. :(
    exit /b 1
)

set "output_name=out"
set "output_dir=%~dp0code\rs\out"

for %%i in ("%~1") do (
    cd "%%~dpi"
    rustc "%%~nxi" -o "%output_dir%\%output_name%.exe"
    "%output_dir%\%output_name%.exe"
)

endlocal
