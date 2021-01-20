def template_py_file(projname):
    content = f'''def main():
    print(\'{projname}\') # Test Print - REMOVE LATER
    
if __name__ == \'__main__\':
    main()'''
    return content


def template_readme_file(projname):
    content = f'''# {projname} 
(Short Description goes here...)
## Contents of this file
* Introduction
* Requirements
* Installation/Configuration
* Authors
* License
* Acknowledgments
## Introduction
(Introduction goes here...)
## Requirements
(Requirements go here (python version, packages to install, etc))
## Installation/Configuration
(Installation steps go here...)
```
Code block example...
```
## Authors
* **André Luz** - [andrefcluz](https://github.com/andrefcluz) - andrefcluz@gmail.com
## License
(Project license if applicable, otherwise N/A)
## Acknowledgments
(Acknowledgments go here...)
'''
    return content