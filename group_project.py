import json
import pathlib


PATH_SAMPLE_DATA = pathlib.Path('sample')


def load_sample_data():
    reddit_posts = []
    for child in PATH_SAMPLE_DATA.iterdir():
        with open(child.name, mode='r', encoding='utf-8') as f:
            post = json.loads(f)
            reddit_posts.append(post)

    return reddit_posts


def main():
    DATA_PATH = pathlib.Path('data/all/train_period_data.jsonlist')

    with open(DATA_PATH, mode='r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    print(len(data))


if __name__ == '__main__':
    main()
