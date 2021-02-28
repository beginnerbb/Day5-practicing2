
import requests
from bs4 import BeautifulSoup


def extract_indeed_pages():
  r=requests.get("https://kr.indeed.com/jobs?q=python")
  b=BeautifulSoup(r.text,"html.parser")

  find_class=b.find("div",{"class":"pagination"})

  get_anchor=find_class.find_all("a")

  list=[]
  list.append(int(find_class.find("li").string))
  """list.append(get_anchor.string)하면 string이 list를 받은 것이 되어 오류뜸. string은 list를 못 받음."""
  
  for n in get_anchor[:-1]:
    list_plus=int(n.string)
    list.append(list_plus)
  last_page=list[-1]
  return last_page
  """get_anchor로 하면 안되고, get_anchor[:-1]로 하면 되는데 왜지??
  get_anchor은 '다음'이 들어가 있고, [:-1]추가하면 '다음'이 포함 안되고 진짜 마지막페이지까지 포함됨. 이 태그에 '다음'이 string이 아니라 태그 속에 포함되어 있는데, 그래서 'NoneType'이라고 나왔던 듯."""

"""
  lists=[]
  lists.append(int(find_class.find("b").string))
  """"""1페이지에서만 필요.. 두번째부터는 1부터 span이더라.."""""""
  for page_number in get_anchor[:-1]:
    lists.append(int(page_number.find("span").string))
  last_page=lists[-1]
  return last_page"""


def extract_indeed_jobs(a):
  for page in range(a):
    URL="&start=(page)*10"
    r=requests.get(f"https://kr.indeed.com/jobs?q=python{URL}")
    pagination=BeautifulSoup(r.text,"html.parser")
    b=pagination.find_all("div",{"class":"jobsearch-SerpJobCard unifiedRow row result clickcard"})
    print(b)
    for n in b:
      c=b.string
      print(c)




"""
def extract_indeed_jobs(last_page):
  for page in range(last_page):
    URL="&start=(page)*10"
    r=requests.get(f"https://kr.indeed.com/jobs?q=python{URL}")
    print(r.status_code)
"""

