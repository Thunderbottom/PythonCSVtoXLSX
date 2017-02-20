# PythonCSVtoXLSX (CLI + GUI)

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
* Includes a tkinter GUI for batch conversion.

## Usage

* Make sure that all the requirements are satisfied -
	* Python3
	*	xlsxwriter

###### CLI: (Single file conversion)

* Run the script - `py csvxl.py`
* The script will then run you through all the steps that need to be followed in order to create the XLS document.


###### GUI: (Batch file conversion)

* Run the GUI script - `py GUI.py`
* Type the path to the CSV files folder, or select the folder by browsing.
* Select whether or not the first line of the CSV is a header.
* Press convert and wait. The script may take some time depending on how much files are being converted.
* Logs are stored inside the `logs/` directory, and the output is stored inside the `output/` directory.


## TODO

- [X] Handle Batch conversion.
- [X] GUI
- [ ] Concatenate multiple CSV files to one XLS document.
- [ ] Custom output directory.
- [ ] More to come..


## License

The MIT License:
```
Copyright (c) 2017 Chinmay Pai

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
