import sys
import os
from github import Github

import templates

def main():

    # Builds the new folder path and gets the Git token
    foldername = str(sys.argv[1])
    path = os.environ.get('proj_path')         # add projects directory to the env vars
    token = os.environ.get('git_token')        # add github token to the env vars
    _dir = path + '\\' + foldername

    # Creates the new Git Repo
    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(foldername, private=True)

    # Create the new folder for the project
    os.mkdir(_dir)
    os.chdir(_dir)

    # Create a main.py file and add the main function
    file_path = _dir + '\main.py'
    file_content = templates.template_py_file(foldername)
    f = open(file_path, "w", encoding='utf-8')
    f.write(file_content)
    f.close()

    # Create a README file
    file_path = _dir + '\README.md'
    file_content = templates.template_readme_file(foldername)
    f = open(file_path, "w", encoding='utf-8')
    f.write(file_content)
    f.close()

    # Creates a list with the git commands to execute
    commands = ['git init',
                f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    # Executes the git commands
    for c in commands:
        os.system(c)

    # Prints a sucess message
    print(f'{foldername} created locally')

    # Opens the new project folder
    # os.startfile(_dir)

    # Open VSCode
    code_command = f'''code "{_dir}"'''
    os.system(code_command)

if __name__ == '__main__':
    main()    