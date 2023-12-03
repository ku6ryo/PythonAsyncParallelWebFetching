import requests
from concurrent.futures import ThreadPoolExecutor

def fetch(url: str):
    response = requests.get(url)
    return response.text

def para_fetch(urls: str):
    with ThreadPoolExecutor() as executor:
        html_contents = list(executor.map(fetch, urls))
    return html_contents

