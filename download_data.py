"""
Download the ChangeMyView Dataset (if needed) and load the records as 
JSON objects.  
"""
from bz2 import BZ2File
import json
import pathlib
import shutil
import tarfile
import requests


CMV_FILE = 'cmv.tar.bz2'
URL = f'https://chenhaot.com/data/cmv/{CMV_FILE}'

# Paths to each data file in CMV_FILE
DATASETS = {  
    'train_period_data': 'all/train_period_data.jsonlist.bz2', 
    'heldout_period_data': 'all/heldout_period_data.jsonlist.bz2', 
    'heldout_op_data': 'op_task/heldout_op_data.jsonlist.bz2', 
    'train_op_data': 'op_task/train_op_data.jsonlist.bz2', 
    'heldout_pair_data': 'pair_task/heldout_pair_data.jsonlist2', 
    'train_pair_data': 'pair_task/train_pair_data.jsonlist.bz2'
}


def download_dataset(url, destination):
    with requests.get(url, stream=True) as r:
        with destination.open(mode='wb') as f:
            shutil.copyfileobj(r.raw, f)


def load_dataset(filename):
    """Open and yield contents of a CMV data file.

    The dataset is downloaded if needed.

    Args:
        filename (str): The name of a data file in the ChangeMyView 
            dataset.

    Yields:
        Deserialized JSON objects for each row of the file.

    Raises:
        FileNotFoundError: The filename parameter cannot be found in
            the DATASETS constant.

    """
    if not DATASETS.get(filename):
        raise FileNotFoundError((
            f'Cannot find dataset: {filename}.\n'
            f'Try one of the following:\n\t'
            f'{"\n\t".join(DATASETS.keys())}'
        ))
    
    cmv_file = pathlib.Path(CMV_FILE) 
        
    if not cmv_file.is_file():
        download(URL, cmv_file)
        
    with cmv_file.open(mode='rb') as f:
        with tarfile.open(f, mode='r') as tar:
            extracted = tar.extractfile(DATASETS[filename])
            for line in BZ2File(extracted):
                yield json.loads(line)
