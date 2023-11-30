# pull_input.py

import os
import shutil
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
        start_year,
        end_year):
    for y in range(start_year, end_year + 1):
        if not os.path.exists(str(y)):
            os.mkdir(str(y))

        for d in range(25):
            day = d + 1
            day_str = str(day).zfill(2)

            print('pulling', y, day_str)

            day_folder = os.path.join(str(y), day_str)

            if not os.path.exists(day_folder):
                os.mkdir(day_folder)

            data = get_data(day=day, year=y)

            with open(os.path.join(day_folder, 'input.txt'), 'w') as f:
                f.write(data)

            print(y, day_str, 'pulled successfully')

            copy_template(day_folder, 'p1.py')
            copy_template(day_folder, 'p2.py')

            time.sleep(.5)


if __name__ == '__main__':
    main(2015, 2023)

