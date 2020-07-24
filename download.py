import json
import os
from glob import glob
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from typing import List, Tuple
from urllib.error import HTTPError

import wget
from natsort import natsorted
from tqdm import tqdm

input_dir = 'beer-database'
output_dir = 'download'
mt = True

icon_output_dir = os.path.join(output_dir, 'icon')
medium_output_dir = os.path.join(output_dir, 'medium')
large_output_dir = os.path.join(output_dir, 'large')
bar = tqdm()

if not os.path.exists(icon_output_dir):
    os.makedirs(icon_output_dir)
if not os.path.exists(medium_output_dir):
    os.makedirs(medium_output_dir)
if not os.path.exists(large_output_dir):
    os.makedirs(large_output_dir)


def parallel_function(f, sequence: List[Tuple[str, str, str]], num_threads=None):
    pool = ThreadPool(processes=num_threads)
    result = pool.map(f, sequence)
    cleaned = [x for x in result if x is not None]
    pool.close()
    pool.join()
    return cleaned


def download_icon_medium_large(web_links: Tuple[str, str, str]):
    download(web_links[0], icon_output_dir)
    download(web_links[1], medium_output_dir)
    download(web_links[2], large_output_dir)


def download(web_link: str, output_directory: str):
    try:
        if not os.path.exists(os.path.join(output_directory, os.path.basename(web_link))):
            wget.download(web_link, output_directory, bar=None)
            # print('-', web_link, 'DOWNLOADED')
        else:
            pass
            # print('-', web_link, 'ALREADY THERE')
    except HTTPError as e:
        print('ERROR', str(e))
    finally:
        bar.update(1)


def main():
    all_files = natsorted(glob(input_dir + '/*.json'))
    all_links = []
    for i, filename in enumerate(all_files):
        with open(filename, encoding='utf8') as r:
            b = json.load(r)
            for record in b['data']:
                all_links.append(
                    (str(record['labels']['icon']),
                     str(record['labels']['medium']),
                     str(record['labels']['large']))
                )
    bar.total = len(all_links) * 3
    if mt:
        parallel_function(download_icon_medium_large, all_links, num_threads=cpu_count())
    else:
        for web_link in all_links:
            download_icon_medium_large(web_link)
    print('Done.')


if __name__ == '__main__':
    main()
