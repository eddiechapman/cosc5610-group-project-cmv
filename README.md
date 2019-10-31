# Change My View

> Network analysis of the Reddit ChangeMyView dataset.


## Installation

```bash
$ git clone https://github.com/eddiechapman/cosc5610-group-project-cmv.git
$ cd cosc5610-group-project-cmv
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 setup.py install
```

## Project structure

```
cosc5610-group-project/
    cmv/
        data/
        __init__.py
        cmv_data.py
        fetch_data.py
        models.py
        parse_data.py
    docs/
    example_data/
    MANIFEST.in
    README.md
    setup.py
```

## TODO

fetch records
- returns a list of json objects of submissions that fall between two dates

download data
- downloads and unzips the dataset if it doesn't already exist in the project directory

models.py
- contrains the object definitions for interacting with the data 

parse_data.py
- creates python objects from models.py using a list of json objects


## Contributing

**Basic Shared Repository Workflow**  
*from https://uoftcoders.github.io/studyGroup/lessons/git/collaboration/lesson/*

- update your local repo with the latest changes from the GitHub repository:
    `git pull origin master`
- create a working branch: 
    `git checkout -b [BRANCH NAME]`
- make your changes: edit code, create new files, delete files
- stage the changes:
    `git add [FILENAME or .]`
- commit your changes locally: 
    `git commit -m "[COMMIT MESSAGE]"`
- upload the changes (including your new branch) to GitHub:
    `git push origin [BRANCH NAME]`
- Go to the main repo on GitHub where you should now see your new branch
- click on your branch name
- click on “Pull Request”
- click on “Send Pull Request”

