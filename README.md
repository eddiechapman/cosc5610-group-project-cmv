## TODO

fetch records
- returns a list of json objects of submissions that fall between two dates

download data
- downloads and unzips the dataset if it doesn't already exist in the project directory

models.py
- contrains the object definitions for interacting with the data 

parse_data.py
- creates python objects from models.py using a list of json objects


## Collaborating

**Basic Shared Repository Workflow**  
*from https://uoftcoders.github.io/studyGroup/lessons/git/collaboration/lesson/*

- update your local repo with git pull origin master,
- create a working branch with git checkout -b MyNewBranch
- make your changes on your branch and stage them with git add,
- commit your changes locally with git commit -m "description of your commit", and
- upload the changes (including your new branch) to GitHub with git push origin MyNewBranch
- Go to the main repo on GitHub where you should now see your new branch
- click on your branch name
- click on “Pull Request” button (URC)
- click on “Send Pull Request”
