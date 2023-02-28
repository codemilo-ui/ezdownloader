import urllib.request

def download(url, filename=None):
    if not filename:
        filename = url.split('/')[-1]

    print(f"Downloading file from {url} to {filename}")
    urllib.request.urlretrieve(url, filename)
    print("File downloaded successfully!")
