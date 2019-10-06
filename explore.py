#%%
import json
import pathlib

examples_dir = pathlib.Path('example_data')

reddit_data = []

for child in examples_dir.iterdir():
    with open(child, mode='r', encoding='utf-8') as f:
        reddit_data.append(json.load(f))

print(len(data))