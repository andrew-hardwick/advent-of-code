# pull_input.py

import os
import shutil
import sys
import time

from aocd import get_data


def copy_template(
        target_folder,
        script):
    target = os.path.join(target_folder, script);
    
    if os.path.exists(target):
        return

    source = os.path.join('template', script)

    shutil.copy(source, target)

def main(
        year,
        day):
    if not os.path.exists(str(year)):
        os.mkdir(str(year))

    day_str = str(day).zfill(2)

    print('pulling', year, day_str)

    day_folder = os.path.join(str(year), day_str)

    if not os.path.exists(day_folder):
        os.mkdir(day_folder)

    data = get_data(day=day, year=year)

    with open(os.path.join(day_folder, 'input.txt'), 'w') as f:
        f.write(data)

    print(year, day, 'pulled successfully')

    copy_template(day_folder, 'p1.py')
    copy_template(day_folder, 'p2.py')


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

