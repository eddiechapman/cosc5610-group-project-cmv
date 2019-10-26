# load the data
import tarfile
import os.path
import json
import re
from bz2 import BZ2File
from urllib import request
from io import BytesIO

import numpy as np
from IPython.display import Markdown

fname = "cmv.tar.bz2"
url = "https://chenhaot.com/data/cmv/" + fname

# download if not exists
if not os.path.isfile(fname):
    f = BytesIO()
    with request.urlopen(url) as resp, open(fname, 'wb') as f_disk:
        data = resp.read()
        f_disk.write(data)  # save to disk too
        f.write(data)
        f.seek(0)
else:
    f = open(fname, 'rb')


tar = tarfile.open(fileobj=f, mode="r")

# Extract the file we are interested in

train_fname = "op_task/train_op_data.jsonlist.bz2"
test_fname = "op_task/heldout_op_data.jsonlist.bz2"

train_bzlist = tar.extractfile(train_fname)

# Deserialize the JSON list
original_posts_train = [
    json.loads(line.decode('utf-8'))
    for line in BZ2File(train_bzlist)
]

test_bzlist = tar.extractfile(test_fname)

original_posts_test = [
    json.loads(line.decode('utf-8'))
    for line in BZ2File(test_bzlist)
]
f.close()

def show_post(cmv_post):
    md_format = "**{title}** \n\n {selftext}".format(**cmv_post)
    md_format = "\n".join(["> " + line for line in md_format.splitlines()])
    return Markdown(md_format)

show_post(original_posts_train[200])