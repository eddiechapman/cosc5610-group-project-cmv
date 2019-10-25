import csv
import datetime
import json
import logging
import pathlib 
import pprint
import parse_data as pd

from models import Submission, Comment, User, BOTLIST, DATE_START, DATE_END

#TO DO: Go through list, apply function or check value --> If return true.
# filterSubmissionsByTime: list of submission objects, startTime (datetime), endTime (datetime) --> list of submission objects
def filterSubmissionsByTime(JSONList):
    submissions = []
    for i in range(len(JSONList)): 
        submissions.append(pd.create_submission(JSONList[i]))
    
    for i in range(len(submissions)):
        print(submissions[i].time)


def grabTimeFromJSON(JSONList):
    for i in range(len(JSONList)):
        print(JSONList[i].keys())

# filterJSONListByTime: jsonlist, startime (datetime), endtime (datetime) --> jsonlist


data = pd.load_examples()
grabTimeFromJSON(data)