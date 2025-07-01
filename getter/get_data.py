import requests

def request_data(url):
    data = requests.get(url)
    print(data.text)