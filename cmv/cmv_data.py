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

DATA_FILE = 'cmv.tar.bz2'
URL = f'https://chenhaot.com/data/cmv/{DATA_FILE}'

p = pathlib.Path(__name__)
DATA = p.parent / 'data'
CMV = DATA / DATA_FILE

# Paths to each data file in CMV_FILE
DATASETS = {  
    'train_period_data': 'all/train_period_data.jsonlist.bz2', 
    'heldout_period_data': 'all/heldout_period_data.jsonlist.bz2', 
    'heldout_op_data': 'op_task/heldout_op_data.jsonlist.bz2', 
    'train_op_data': 'op_task/train_op_data.jsonlist.bz2', 
    'heldout_pair_data': 'pair_task/heldout_pair_data.jsonlist2', 
    'train_pair_data': 'pair_task/train_pair_data.jsonlist.bz2'
}


def download():
    """
    Download the CMV dataset to cmv/data/cmv.tar.bz2.
    """
    DATA.mkdir(exist_ok=True)

    if CMV.exists():
        raise FileExistsError(f'Dataset found: {CMV}. Download aborted.')
    
    with requests.get(URL, stream=True) as r:
        with CMV.open(mode='wb') as f:
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
        new_line = '\n'
        new_line_tab = '\n\t'
        raise FileNotFoundError((
            f'Cannot find dataset: {filename}.{new_line}'
            f'Try one of the following:{new_line_tab}'
            f'{new_line_tab.join(DATASETS.keys())}'
        ))
        
    with CMV.open(mode='rb') as f:
        with tarfile.open(f, mode='r') as tar:
            extracted = tar.extractfile(DATASETS[filename])
            for line in BZ2File(extracted):
                yield json.loads(line)
