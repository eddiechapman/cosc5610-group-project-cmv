import json
import pathlib


def read_json_dir(path):
    """
    Read a directory of json files as a list of dictionaries.
    """
    reddit_data = []
    for child in path.iterdir():
        with open(child.name, mode='r', encoding='utf-8') as f:
            post = json.loads(f)
            reddit_data.append(post)

    return reddit_data


def read_jsonfile(path):
    """
    Read a jsonfile (one json per line) file as a list of dictionaries.
    """
    with open(path, mode='r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]


def write_example_files(data, path):
    """
    Save a subset of the main dataset to a directory as json files.
    """
    filenames = [f'example{i}.json' for i, _ in enumerate(data, 1)]
    for json_data, name in zip(data, filenames):
        with open(path / name, 'w') as f:
            json.dump(json_data, f)


if __name__ == '__main__':
    pass
