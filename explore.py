#%%
import json
import pathlib


reddit_data = []
examples_dir = pathlib.Path('example_data')
example2 = examples_dir / 'example2.json'
for child in examples_dir.iterdir():
    with open(child, mode='r', encoding='utf-8') as f:
        print(json.load(f))
# for child in examples_dir.iterdir():
#     with child.open(mode='r', encoding='utf-8') as f:
#         print(f)
#         print([line for line in f])
#         print(json.load(f))
        # post = json.load(f)
        # reddit_data.append(post)

print(len(data))




#%%
