## API JSON Downloader
This is a program that fetches data from an API (usually in JSON format), and downloads it.

## Usage
```
$ python3 download.py --help
usage: download.py [-h] [-n FILENAME] [-fo FOLDEROUTPUT] [-o OUTPUT] url

Get information from an API and download it.

positional arguments:
  url                   Input URL of API you would like to download.

options:
  -h, --help            show this help message and exit
  -n FILENAME, --name FILENAME
                        Specify name of the text file to be created. Default will be example.com.txt
  -fo FOLDEROUTPUT, --folderoutput FOLDEROUTPUT
                        Specify directory to where it will be downloaded.
  -o OUTPUT, --output OUTPUT
                        Specify directory to an existing text file, it will be overwritten.
```
For example:
```
$ python3 download.py https://aws.random.cat/meow -n meow 
```
This downloads the data from https://aws.random.cat/meow and names it meow(.txt).