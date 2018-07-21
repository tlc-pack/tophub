"""make metainfo `info.json` for the parameter files"""

import argparse
import json
import os
import hashlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", type=str, default=".")
    args = parser.parse_args()

    lib = {}

    for filename in os.listdir(args.i):
        if filename.endswith(".log"):
            target = filename[:-4]
            size = os.path.getsize(filename)
            mtime = os.path.getmtime(filename)
            md5 = hashlib.md5(open(filename, 'rb').read()).hexdigest()

            lib[target] = {'size': size, 'mtime': mtime, 'md5': md5}

    with open("info.json", "w") as fout:
        json.dump(lib, fout, sort_keys=True,
                  indent=4, separators=(',', ':'))

