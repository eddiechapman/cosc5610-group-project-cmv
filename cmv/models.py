import datetime

BOTLIST = ['DeltaBot']
DATE_START = datetime.datetime(year=2013, month=1, day=1)
DATE_END = datetime.datetime(year=2015, month=8, day=31)

class Submission:
    def __init__(self):
        self.id = None
        self.op = None
        self.title = None
        self.text = None
        self.time = None
        self.comments = []

    def iter_comments(self):
        return (c for c in self.comments if c.is_challenger())

    @property
    def affiliates(self):
        """Return the names of unique participants in the thread."""
        return list(set(c.author for c in self.iter_comments()))

    def __str__(self):
        return(
            f'=============================================\n'
            f'{self.title}\n'
            f'posted by {self.op} on {self.time}\n'
            f'{len(list(c for c in self.comments if c.is_challenger()))} comments\n'
            f'---------------------------------------------\n'
            f'{self.text}\n'
            f'---------------------------------------------\n'
        )


class Comment:
    def __init__(self):
        self.id = None
        self.author = None
        self.text = None
        self.parent = None
        self.parent_op = None

    def is_challenger(self):
        """Is the comment author a unique challenger on the thread?"""
        return self.author not in BOTLIST + [self.parent_op] + ['[DELETED]']

    def __str__(self):
        return(
            f'{self.author}\n'
            f'Reply to submission {self.parent} by OP {self.parent_op}\n'
            f'---------------------------------------------\n'
            f'{self.text}\n'
        )


class User:
    def __init__(self):
        self.name = None
        self.comments = []
        self.affiliations = set()
    
    def update_affiliations(self, comment_store):
        for comment_id in self.comments:
            comment = comment_store.get(comment_id)  
            if comment:
                self.affiliations.add(comment.parent)

    def __str__(self):
        return(
            f'{self.name}\n'
            f'{", ".join(self.affiliations)}\n'
        )