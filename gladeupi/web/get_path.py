from urllib.parse import urlparse
def get_path(url):
    return urlparse(url).path