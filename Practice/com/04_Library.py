# from urllib.request import urlopen
import urllib.request

url = "https://www.nate.com/"
html = urllib.request.urlopen(url)

print(html.read())