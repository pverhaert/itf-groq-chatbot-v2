@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Display a message to the user
echo Running Streamlit application...
echo To stop the Streamlit application, press Ctrl+C in this window.

REM Run the Streamlit application
streamlit run main.py

echo To stop the Streamlit application, press Ctrl+C in this window.

REM Pause the command prompt to see any output or errors
pause