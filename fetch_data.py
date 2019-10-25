import csv
import datetime
import json
import logging
import pathlib
import pprint

#from models import Submission, Comment, User, BOTLIST, DATE_START, DATE_END

# filterSubmissionsByTime: list of submission objects, startTime (datetime), endTime (datetime) --> list of submission objects
def filterSubmissionsByTime(submissionList, startTime, endTime):
    for submission in submissionList:

# filterJSONListByTime: jsonlist, startime (datetime), endtime (datetime) --> jsonlist