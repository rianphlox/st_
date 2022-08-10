from bs4 import BeautifulSoup
import requests, sys
from params import credentials

url = "https://www.christembassysoultracker.org/"
client = requests.session()
client.get(url)
if "csrf_cookie_name" in client.cookies:
    csrftoken = client.cookies['csrf_cookie_name']
    # print(csrftoken)
login_data = dict(username=credentials['username'], password=credentials['password'], csrfmiddlewaretoken=csrftoken, next='/')
r = client.post(url, data=login_data, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
print(r.text)