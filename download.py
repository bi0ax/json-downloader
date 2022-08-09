import requests
import json
from pathlib import Path
import argparse
from urllib.parse import urlparse
parser = argparse.ArgumentParser(description="Get information from an API and download it.")
parser.add_argument("url", type=str, help="Input URL of API you would like to download.")
parser.add_argument("-n", "--name", type=str, metavar="FILENAME", help="Specify name of the text file to be created. Default will be example.com.txt")
parser.add_argument("-fo", "--folderoutput", type=str, help="Specify directory to where it will be downloaded. ")
parser.add_argument("-o", "--output", type=str, help="Specify directory to an existing text file, it will be overwritten.")
args = parser.parse_args()
response = requests.get(args.url)
if response.status_code != 200:
    print(f"Something went wrong. Status Code: {response.status_code}")
else:
    response_json = json.loads(response.text)
    new_file_name = args.name
    download_path = Path("downloads/")
    new_file = True
    if not args.name: 
        domain = urlparse(args.url).netloc
        new_file_name = domain.split(".")[-2] + "." + domain.split(".")[-1]
    if args.folderoutput:
        download_path = Path(args.folderoutput)
    if args.output:
        download_path = Path(args.output)
        with open(download_path, "w") as json_write:
            json_write.write(json.dumps(response_json))
    else:  
        download_path = download_path / (f"{new_file_name}.txt")
        with open(download_path, "w") as json_write:
            json_write.write(json.dumps(response_json))
    print(f"Success! Wrote the data from {args.url} to {download_path}")