import requests
import re

import matplotlib.pyplot as plt


def main():
    r = requests.get('https://web.archive.org/cdx/search/cdx?url=tinypic.com/view.php*&output=json')
    ids_ = []
    last = [0, False]
    for d in r.json():
        if d[4] != "200":
            continue
        find = re.search('(?:pic|v)=([a-zA-Z0-9]+)&s=3', d[2])
        if not find:
            continue
        ids_.append(int(find.group(1), 36))
    ids = []
    for i in sorted(ids_):
        if i - last[0] > 100000:
            if last[1] == False:
                last[1] = True
                print(i)
        else:
            last = [i, False]
        ids.append(i)
    print(len(ids))
    print(max(ids))
    plt.hist(ids, 10000)
    plt.show()

if __name__ == '__main__':
    main()

