import csv
import datetime
import json
import logging
import pathlib 
import pprint
import parse_data as pd

from models import Submission, Comment, User, BOTLIST, DATE_START, DATE_END

#getMatchesFromJSON: 
    #input: JSONlist, field to query, list of conditions.
    #output: List of json strings with matching field.
def getMatchesFromJSON(JSONList, field, conditions):
    matchingJSON = []
    for i in range(len(JSONList)):
        currentRow = JSONList[i]
        if field == "created_utc":
            dateTimeObj = datetime.datetime.fromtimestamp(currentRow['created_utc'])
            stringDate = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
            if(stringDate in conditions): 
                matchingJSON.append(currentRow)
        elif (currentRow[field] in conditions):
            matchingJSON.append(currentRow)
    return matchingJSON

#filterMatchesByDatetime
    #input: JSONlist, (String) start datetime, (String) end datetime.
    #Output: list of json strings with time in range
def filterMatchesByDatetime(JSONList, startTime, endTime):
    matchingJSON = []
    if (type(startTime) is str): startTime = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    if (type(endTime) is str): endTime = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    for i in range(len(JSONList)):
        currentRow = JSONList[i]
        dateTimeObj = datetime.datetime.fromtimestamp(currentRow['created_utc'])
        if (dateTimeObj > startTime and dateTimeObj < endTime): matchingJSON.append(currentRow)
        #if (dateTimeObj > startTime and dateTimeObj < endTime): matchingJSON.append(datetime.datetime.fromtimestamp(currentRow['created_utc']))
            #Uncomment to validate that correct instances being retrieved
    return matchingJSON

#applyFunctionToAllRows
    #input: name of function to be applied to each item, JSONList
    #output

data = pd.load_examples()
matchingTime = getMatchesFromJSON(data, "created_utc", ['2015-01-07 18:25:30'])
