# Machine_learning_practice

### software and Account Requirements.

1. Github Account
2. Heroku Account
3. VS code IDE
4. GIT cli

creating conda envirement

'''
conda create -p venv python==3.7 -y
'''
conda activate venv/
'''

to add files to git
'''
git add .
'''
or
'''
git add file_name
'''

to ingnore file or folder we use file name in gitignore file


to check git status
'''
git status
'''

to check all version maintain by git
'''
git log
'''

to crate version/commite all changes by git
'''
git commit -m "message"
'''

to send version/changes to github
'''
git push origin main
'''

to check remote url
'''
git remote -v
'''

To setup CI/CD pipeline in heroku we need 3 information:

1. Heroku Email= nikumbhmohit@gmail.com
2. Heroku Api key = <>
3. HEROKU_APP_NAME=ml-regression-m



BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tag_name> .
'''
> NOTE: Image name for docker must be lowercase



Housing is root folder of project we write our main project code inside it

'''
-e . trying to take care things whuch is not installed it install everithing which neede to be install.
'''