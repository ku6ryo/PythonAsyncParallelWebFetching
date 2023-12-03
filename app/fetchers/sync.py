import requests

def fetch(url: str):
    response = requests.get(url)
    return response.text

def multi_fetch(urls: str):
    html_contents = []
    for url in urls:
        html_contents.append(fetch(url))
    return html_contents
