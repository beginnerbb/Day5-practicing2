
"""import requests
from bs4 import BeautifulSoup

r=requests.get("https://kr.indeed.com/jobs?q=python")
b=BeautifulSoup(r.text,"html.parser")

find_class=b.find("div",{"class":"pagination"})

get_anchor=find_class.find_all("a")

lists=[]
lists.append(int(find_class.find("b").string))
1페이지에서만 필요.. 두번째부터는 1부터 span이더라...

for page_number in get_anchor[:-1]:
  lists.append(int(page_number.find("span").string))
print(lists)

for page in lists:
  URL="&start=(page-1)*10"
  r=requests.get(f"https://kr.indeed.com/jobs?q=python{URL}")
  print(r.status_code)"""
