import csv
import datetime
import json
import logging
import pathlib
import pprint

from models import Submission, Comment, User, BOTLIST, DATE_START, DATE_END

PATH_EXAMPLE_DIR = pathlib.Path('example_data')
PATH_ALL_DATA = pathlib.Path('data/all/heldout_period_data.jsonlist')


def load_examples():
    data = []
    for child in pathlib.Path('example_data').iterdir():
        with open(child, mode='r', encoding='utf-8') as f:
            data.append(json.load(f))
    
    return data


def load_all_data(path):
    """
    Read a jsonfile (one json per line) file as a list of dictionaries.
    """
    with open(path, mode='r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]


def create_submission(data):
    try:
        submission_id = data['id']
    except KeyError:
        raise KeyError('No ID found in JSON object.')
    
    submission = Submission()
    submission.id = submission_id

    try: 
        submission.title = data['title']
        submission.op = data['author']
        submission.text = data['selftext']
        submission.time = datetime.datetime.fromtimestamp(data['created_utc'])
    except KeyError:
        raise KeyError(f'Missing attributes in submission {submission.id}')

    return submission


def create_comment(data, submission):           
    try:
        comment_id = data['id']
    except KeyError:
        raise KeyError(f'No ID for comment found in submission {submission.id}')
    
    comment = Comment()
    comment.id = comment_id
    comment.parent = submission.id
    comment.parent_op = submission.op
    
    try:
        comment.author = data['author']
        comment.text = data['body']
    except KeyError:
        raise KeyError(f'Missing attributes in comment {comment.id}')

    return comment


def extract_submissions(reddit_data):
    """
    Return dictionaries containing reddit submissions, comments and users.
    """
    submissions = {}
    for submission_data in reddit_data:
        try:
            submission = create_submission(submission_data)
        except KeyError as e:
            logging.error(e)
        else:
            for comment_data in submission_data['comments']:
                try:
                    comment = create_comment(comment_data, submission)
                except KeyError as e:
                    logging.error(e)
                else:
                    submission.comments.append(comment)
            
            submissions[submission.id] = submission
    
    return submissions


def extract_comments(submission_store):
    comments = {}
    for submission in submission_store.values():
        for comment in submission.iter_comments():
            comments[comment.id] = comment
    
    return comments


def extract_users(comment_store):
    users = {}
    for comment in comment_store.values():
        user = users.get(comment.author)
        if not user:
            user = User()
            user.name = comment.author
        user.comments.append(comment.id)
        users[comment.author] = user

    for user in users.values():
        user.update_affiliations(comment_store)

    return users
    

def write_affiliation_table(user_store):
    with open('affiliations.csv', 'w') as f:
        writer = csv.writer(f)
        for user in user_store.values():
            for submission in user.affiliations:
                writer.writerow([user.name, submission])


def filter_submissions_by_date(submission_store, start=DATE_START, end=DATE_END):
    filtered = []
    for submission in submission_store.values():
        if submission.time >= start and submission.time <= end:
            filtered.append(submission.id)

    return filter_dict(submission_store, filtered)
        

def filter_dict(source, selections):
    """Return a subset of a dictionary based on a key list"""
    return {k: source[k] for k in selections}


if __name__ == '__main__':
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )
    logging.info('Loading reddit data.')
    data = load_all_data(PATH_ALL_DATA)
    
    logging.info('Processing submissions and comments.')
    submissions = extract_submissions(data)
    
    logging.info('Filtering submissions by date')
    start_date = datetime.datetime(year=2015, month=6, day=1)
    end_date = datetime.datetime(year=2015, month=6, day=2)
    filtered_submissions = filter_submissions_by_date(submissions, start_date, end_date)

    logging.info('Extracting comments')
    comments = extract_comments(filtered_submissions)
    
    logging.info('Extracting users')
    users = extract_users(comments)
    
    logging.info('Writing user-submission affiliation table.')
    write_affiliation_table(users)
