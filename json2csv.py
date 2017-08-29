import sys
import csv
import json


def main():

    _json = json.loads(open(sys.argv[1], 'r').read())
    _csv = csv.writer(open(sys.argv[1] + '.csv', 'w'))
    _csv.writerow(_json[0].keys())

    for row in _json:
        _csv.writerow(row.values())


if __name__ == '__main__':
    main()

