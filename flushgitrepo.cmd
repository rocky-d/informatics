@echo off
setlocal

set "script_name=flushgitrepo"

set "current_dir=%cd%"

if not "informatics"=="%current_dir:~-11%" (
    echo %script_name% ^>^> Current directory mismatch. :(
    exit /b 1
)

git rm -r --cached --quiet .
git add .

echo Git repository flushed. :)

endlocal
