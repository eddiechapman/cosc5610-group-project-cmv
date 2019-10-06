import json
import pathlib


PATH_SAMPLE_DATA = pathlib.Path('sample')
PATH_ALL_TRAIN_DATA = pathlib.Path('data/all/train_period_data.jsonlist')


def read_json_dir(path=PATH_SAMPLE_DATA):
    """
    Read a directory of json files as a list of dictionaries.
    """
    reddit_data = []
    for child in path.iterdir():
        with open(child.name, mode='r', encoding='utf-8') as f:
            post = json.loads(f)
            reddit_data.append(post)

    return reddit_data


def read_jsonfile(path=PATH_ALL_TRAIN_DATA):
    """
    Read a jsonfile (one json per line) file as a list of dictionaries.
    """
    with open(path, mode='r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]


if __name__ == '__main__':
    pass
