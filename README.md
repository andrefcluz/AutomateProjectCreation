# AutomateProjectCreation 
Script to automate the creation of new Python projects
## Contents of this file
* Introduction
* Requirements
* Installation/Configuration
* Authors
* License
* Acknowledgments
## Introduction
Script to automate the creation of new Python projects which runs by batch command or (optionally) with a shortcut (using AutoHotKey)
It runs a Python script that creates a folder for the project, a main.py file, a README.me file (with a template), a Github Repository, makes the first commit and lastly it opens the project folder in a new instance of VSCode 
## Requirements
* Computer running Windows
* PyGithub Python module
* Github token
## Installation/Configuration
1. Install the Python modules (pip install -r requirements.txt)

2. Create two system variables:
    * proj_path - Add your projects directory here (the new projects will be created inside this folder)
    * git_token - Add your Github token here (get it on your Github account, under Settings -> Developer settings -> Personal access tokens -> Generate new token)

    If you don't know how to create system variables check this link https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

3. *To run the script with a keyboard shortcut (Optional)*
    * Install [AutoHotKey](https://www.autohotkey.com/)
    * Create a new AHK script (check their tutorial to see how it works)
    * Add the following code to your script, which runs when the key combination CTRL+ALT+SHIFT+N (you can change the combination for whatever you want) is pressed. It opens a dialog box, asking for the project name, and then it runs the script and creates th project with the given input
    ```
    ;Create New Project - CTRL+ALT+SHIFT+N
    ^!+n::
    InputBox, proj_name, New Project, Project Name:, , 300, 130
    If ErrorLevel = 0
        Run <path to the create.bat bash file> %proj_name%
    return
    ```
    * Add the AHT script to the startup folder so it runs when windows starts

## Authors
* **André Luz** - [andrefcluz](https://github.com/andrefcluz) - andrefcluz@gmail.com
## License
N/A
## Acknowledgments
This project is an adaptation of [Kalle Hallden's](https://github.com/KalleHallden) project "ProjectInitializationAutomation", which does almost the same thing. I just changed some things to make it fit better in my workflow

Link to his video: [One Day Builds: Automating My Projects With Python](https://www.youtube.com/watch?v=7Y8Ppin12r4)

Link to his Github repository: [ProjectInitializationAutomation](https://github.com/KalleHallden/ProjectInitializationAutomation)
