import argparse
import requests

def download(url, output):
    response = requests.get(url, stream=True)

    with open(output, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

parser = argparse.ArgumentParser()

parser.add_argument("url", help="URL of the file to download")
parser.add_argument("output", help="Name of the output file")

args = parser.parse_args()

print(args.url)
print(args.output)

download(args.url, args.output)