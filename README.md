# PythonCSVtoXLSX

######Python script to convert CSV to XLSX.

###### Basically, this'll help you convert CSV files to Excel Sheets. 
######The primary goal of creating this was to learn to use Python and understand how the underlying functions and modules work.

###### Pull requests are always appreciated!


## Requirements

* [Python3+](https://www.python.org/downloads/)
* [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)


## Features

* Create XLS sheets from CSV Files.
*	Define custom column names for the spreadsheet.
*	Skip rows with column length lesser than or greater the CSV header column length.
* Custom XLS Filename for output.


## Usage

* Make sure that all the requirements are satisfied -
	* Python3
	*	xlsxwriter
* Run the script - `py csvxl.py`
* The script will then run you through all the steps that need to be followed in order to create the XLS document.


## TODO

- [ ] Handle Batch conversion.
- [ ] Concatenate multiple CSV files to one XLS document.
- [ ] More to come..


## License

The MIT License:
```
Copyright (c) Chinmay Pai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
