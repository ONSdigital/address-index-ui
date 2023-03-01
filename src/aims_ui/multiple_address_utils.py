import requests
import tarfile
import io
import json

# Server-side conversion of the zipfile into a csv download

def extract_json_from_tar_gz(url):
    # Download the file from the URL
    response = requests.get(url)

    # Extract the JSON file from the tar.gz archive
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as tar:
        json_file = tar.extractfile(tar.getmembers()[0]).read()

    # Parse the JSON file and return it as a Python variable
    return json.loads(json_file)

def downloadZipToMemory(url):
  json_content = extract_json_from_tar_gz(url)
  print(json_content)

