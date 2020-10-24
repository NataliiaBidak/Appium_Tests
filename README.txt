This is an instruction of Appium tests launching.
Preconditions:
1.Appium server is running
2.Real device or simulated is conected to your machine.

To run the tests you need:
 1. install requirements.txt (project root folder), run $pip install -r requirements.txt
 2.Set proper path for this project to PROJECT_FOLDER variable in settings.py file (project root folder)
 3.Set proper device capabilities to DESIRED_CAPS variable in settings.py file
 4.Set path to alluredir value in pytest.ini file(project root folder)

 !NOTE! alluredir path must be the same as TEST_REPORTS path settings.py file

 5.If you don't want the allure report to be launched automatically,
 (or if you are experiencingq some troubles with allure configuration on your machine)
 set to False state RUN_REPORT_AUTOMATICALLY value in settings.py file

 Allure report can be generated manually, run $allure serve /home/nbidak/PycharmProjects/PythonAppiumFramework/tests/reports/
 !NOTE! Folder specified in command above has to be the same as alluredir path in step 4.

!!!ENJOY!!!