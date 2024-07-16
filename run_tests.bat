@echo off
call env\scripts\activate
cd tests
py.test --browser_name %browser% --html=%WORKSPACE%/reports/report.html -v --junitxml="result.xml"

