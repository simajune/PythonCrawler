import urllib.request
import bs4

url = "https://naver.com"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("div", {"class": "area_links"})

first_a = top_right.find("a", {"data-clk": "top.mkhome"})

# print(top_right)
print(first_a.text)