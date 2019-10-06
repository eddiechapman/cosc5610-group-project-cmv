import json
import pathlib

def main():
    DATA_PATH = pathlib.Path('data/all/train_period_data.jsonlist')

    with open(DATA_PATH, mode='r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    print(len(data))


if __name__ == '__main__':
    main()
