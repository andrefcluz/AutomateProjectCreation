### pre-setup:
```
create env vars :

> projects directory as - "proj_path"
> Github tocken as      - "git_token"
```
https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

### setup: 
```bash
git clone "https://github.com/wikyprash/projectInitializerAutomation.git"
cd projectInitializerAutomation
pip install -r requirements.txt

path:
"projectInitializerAutomation" folder directory to path
```

### Usage:
```bash
Command to run the program type

'create <project_name>'
```

### Usage AutoHotKey
Update bash path in AHK script Google Drive/01.Personal/Others/Scripts
CTRL+ALT+SHIFT+N

;Create New Project - CTRL+ALT+SHIFT+N
^!+n::
InputBox, proj_name, New Project, Project Name:, , 300, 130
If ErrorLevel = 0
    Run <path to bash> %proj_name%
return