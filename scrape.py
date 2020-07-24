import json
import os
import sys
from glob import glob

from natsort import natsorted

from beer_api import BreweryDb

output_dir = 'beer-database'


def main():
    if len(sys.argv) <= 1:
        print('Specify api_key as argument.')
        exit(1)
    api_key = sys.argv[1]
    BreweryDb.configure(apikey=api_key, baseuri='https://api.brewerydb.com/v2/')
    page = get_last_page() + 1
    print(f'Restarting from: {page}')
    for i in range(page, 100000):
        b = BreweryDb.beers({'p': i, 'hasLabels': 'Y'})
        if 'errorMessage' in b:
            print('ERROR:', b['errorMessage'])
            exit(1)
        elif 'data' not in b:
            print('FINISHED.')
            exit(1)
        else:
            persist(b)


def get_last_page():
    try:
        return int(os.path.splitext(os.path.basename(natsorted(glob(output_dir + '/*.json'))[-1]))[0].split('_')[-1])
    except:
        return 0


def persist(b: json):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    current_page = b['currentPage']
    output_filename = os.path.join(output_dir, f'beer_{current_page}.json')
    print('-', output_filename)
    with open(output_filename, 'w', encoding='utf-8') as w:
        json.dump(obj=b, fp=w, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
