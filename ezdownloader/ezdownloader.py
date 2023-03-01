import argparse
import os
from urllib.request import urlretrieve
import sys


def download(url, filename=None, path=None, overwrite=False):
    def progress(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write(f"\rDownloading {filename}: [{percent:>3}%] ")
        sys.stdout.flush()

    if path is None:
        path = os.getcwd()

    if filename is None:
        filename = url.split('/')[-1]

    full_path = os.path.join(path, filename)

    if os.path.isfile(full_path) and not overwrite:
        response = input(
            f"File '{full_path}' already exists. Overwrite? [y/n] ")
        if response.lower() != 'y':
            print("Download canceled.")
            return None

    if not os.path.isdir(path):
        os.makedirs(path)

    urlretrieve(url, full_path, progress)
    return full_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='the URL of the file to download')
    parser.add_argument('-f', '--filename',
                        help='the name of the file to save as')
    parser.add_argument(
        '-p', '--path', help='the directory to save the file in')
    parser.add_argument('-o', '--overwrite',
                        action='store_true', help='overwrite existing files')
    args = parser.parse_args()

    filename = args.filename
    if filename is not None and isinstance(filename, str):
        filename += str(args.url)

    path = args.path
    if path is not None and not os.path.isdir(path):
        print(f"Invalid path: {path}")
        return

    full_path = download(args.url, filename, path, args.overwrite)

    if full_path is not None:
        print(f"File '{full_path}' downloaded successfully.")
