#!/usr/bin/env python3

import xlsxwriter as xl
import csv
import os
import linecache

def checkLog(logname):
    checkLog = os.path.isfile(logname)
    if checkLog:
        os.remove(logname)


def convert(filename, path, check, openFile):
    rowNo = 2
    line = linecache.getline(path+ '/' + filename, 1)
    columnLength = len(line)
    if not check:
        columnNames = []
        for x in range(1, int(columnLength) + 1):
            cName = ''
            columnNames.append(cName)
    else:
        columnNames = next(openFile)
        #columnLength = len(columnLength) TODO: Redundant I guess..
    if not os.path.exists('output/'):
        os.makedirs('output/')
    workbook = xl.workbook.Workbook('output/' + filename + '.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True})
    worksheet.set_row(0, 15, cell_format)
    worksheet.write_row('A1', columnNames)
    # Write data from CSV to XLS
    try:
        totalLines = 0
        skipped = 0
        for row in openFile:
            if not len(row) < int(columnLength) or len(row) > int(columnLength):
                worksheet.write_row('A' + str(rowNo), row)
                rowNo += 1
                totalLines += 1
            else:
                skipped += 1
    except Exception as e:
        print(e)
        return 1
    workbook.close()
    logf = open('logs/output.log', 'a')
    logf.write('Successfully wrote file: ' + filename + '.xlsx\n')
    logf.write('Total lines written:' + str(totalLines) + '.\n')
    logf.write('Total lines skipped:' + str(skipped) + '.\n')
    if skipped:
        logf.write(
            'Lines were skipped as the row length was greater than the header length\n\n')
    logf.close()


def converter(path, files, check):
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    checkLog('logs/error.log')
    checkLog('logs/output.log')
    log = 0
    out = 0
    for filename in files:
        try:
            openFile = csv.reader(open(path + "/" + filename, "r"), quotechar='"',
                                  delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            filename = filename.rsplit(".", 1)[0]
            out = convert(filename, path, check, openFile)
        except Exception as e:
            print(e)
            logf = open('logs/error.log', 'a')
            logf.write('Couldn\'t read file: ' + filename +
                       ' due to some error. Aborted.\n')
            log += 1
            logf.close()
            return 1

    if log or out:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print('You need to run the csvxl.py file to execute the CLI version of the converter.\nOr you may run GUI.py to run the GUI version of the converter')
    exit(0)
