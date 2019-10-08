
#%%
import json
import pathlib
import pprint

examples_dir = pathlib.Path('example_data')

reddit_data = []

for child in examples_dir.iterdir():
    with open(child, mode='r', encoding='utf-8') as f:
        reddit_data.append(json.load(f))


class Comment:
    def __init__(self, json_data):
        self.id = json_data['id']
        self.author = json_data['author']
        if json_data.get('replies'):
            self.children = json_data['replies']['data']['children']
        else:
            self.children = None
        self.name = json_data['name']
        self.text = json_data['body']
        self.parent = json_data['parent_id']

    @property
    def is_bot(self):
        pass

    def __str__(self):
        return (f'ID\t\t\t{self.id}\n'
                f'Author\t\t\t{self.author}\n'        
                f'Name\t\t\t{self.name}\n'
                f'Parent\t\t\t{self.parent}\n'
                f'Children\t\t{self.children}\n')

comments = {}
for comment_data in reddit_data[0].get('comments'):
    comment = Comment(comment_data)
    comments[comment.id] = comment

for c, v in comments.items():
    print(v)




#%%
