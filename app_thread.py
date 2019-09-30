#!/usr/bin/python3

import argparse
from  concurrent.futures import ThreadPoolExecutor
import shutil
import os

def coping_files(posit, dest):
    files = os.listdir(posit)

    for file in files:
        shutil.copy2(posit+file, dest)

def main():
    position = args.position
    destination = args.destination
    max_workers = args.max_workers

    executor = ThreadPoolExecutor(max_workers)
    future = executor.submit(coping_files, position, destination)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--position",
            type=str, required=True,
            help="The position of the directory to copy from")

    parser.add_argument("-d", "--destination",
            type=str, required=True,
            help="The destionation to copy the files to")

    parser.add_argument("-w", "--max_workers",
            type=int, required=False, default=5,
            help="The number of maximum workers")

    args = parser.parse_args()
    main()

