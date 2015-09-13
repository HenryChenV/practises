#-*-coding=utf-8-*-

import csv
import StringIO

def testDictWriter(filename):
    rows = [
        {'Column1': None, 'Column2': 12, 'Column3': 13, 'Column4': 14},
        {'Column1': '21', 'Column2': '22', 'Column4': '24'},
        {'Column1': '31', 'Column2': '32', 'Column1': '31', 'Column4': '34'},
        {'Column1': '41', 'Column3': '43', 'Column2': '42', 'Column4': '44'},
        {'Column1': '51', 'Column2': '52', 'Column3': '53', 'Column4': '54'}
    ]
    field_names = ['Column1', 'Column2', 'Column3', 'Column4']

    with open(filename, 'wb') as fp:
        dict_wtiter = csv.DictWriter(fp, fieldnames=field_names)
        dict_wtiter.writerow(dict(zip(field_names, field_names)))
        dict_wtiter.writerows(rows)


def testDictReader(filename):
    rows = []
    with open(filename, 'rb') as fp:
        dict_reader = csv.DictReader(fp)
        for row in dict_reader:
            rows.append(row)

    import pprint
    pprint.pprint(rows)


def testDictWriterStringIO():
    rows = [
        {'Column1': None, 'Column2': 12, 'Column3': 13, 'Column4': 14},
        {'Column1': '21', 'Column2': '22', 'Column4': '24'},
        {'Column1': '31', 'Column2': '32', 'Column1': '31', 'Column4': '34'},
        {'Column1': '41', 'Column3': '43', 'Column2': '42', 'Column4': '44'},
        {'Column1': '51', 'Column2': '52', 'Column3': '53', 'Column4': '54'}
    ]
    field_names = ['Column1', 'Column2', 'Column3', 'Column4']

    tmp_string = StringIO.StringIO()
    dict_wtiter = csv.DictWriter(tmp_string, fieldnames=field_names)
    dict_wtiter.writerow(dict(zip(field_names, field_names)))
    dict_wtiter.writerows(rows)

    tmp_string.seek(0)
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    print tmp_string.read()


def main():
    filename = 'testdict.csv'
    testDictWriter(filename)
    testDictWriter(filename)
    testDictWriterStringIO()


if __name__ == '__main__':
    main()
