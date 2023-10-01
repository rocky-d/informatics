@echo off
chcp 65001
setlocal enabledelayedexpansion

rem 设置脚本名称（用于输出报错信息）
set "script_name=runcpp"

rem 检查是否提供了文件路径参数
if "%~1"=="" (
    echo !script_name! ^>^> One parameter missing.
    exit /b 1
)

rem 获取文件名（不包含扩展名）
rem for %%i in ("%~1") do set "output_name=%%~ni"
set "output_name=main"

rem 设置编译输出目录
set "output_dir=.\code\cpp\out"

rem 编译C++文件并将可执行文件输出到指定目录
g++ "%~1" -o "%output_dir%\!output_name!.exe"

if errorlevel 1 (
    echo !script_name! ^>^> Fail to compile.
    exit /b 1
)

"%output_dir%\!output_name!.exe"

endlocal
