@echo off
REM Run the data processor with the given input file

IF "%~1"=="" (
    ECHO Usage: run_processor.bat input_file.txt
    PAUSE
    EXIT /B 1
)

python data_processor.py %1

ECHO.
ECHO Press any key to exit...
PAUSE >nul
