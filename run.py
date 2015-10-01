# -*- coding: utf-8 -*-
import requests
import sys
import re
from multiprocessing import Pool



def isurl(s):
    if re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', s):
        return True
    else:
        return False

  
def getPermalink(url):
  # will need to handle cases that it can't find, like for http://w3techs.com/technologies/overview/javascript_library/all
  if 'web.archive' in url:
    return url,url
  try:
    r = requests.get('https://web.archive.org/save/' + url)
  except:
    return url,url
  if r.status_code == 403:
    return url,url
  else:
    return url,'https://web.archive.org' + r.headers['content-location']
  

def replaceText(text_test):
  newurls = []
  for url in  re.findall(r'(https?://[^\s]+)', text_test):
    newurl = url
    while newurl[-1] == '.' or newurl[-1] == ')' or newurl[-1] == '!':
      newurl = newurl[:-1]
    newurls.append(newurl)

  p = Pool(10)
  for result in p.map(getPermalink,newurls):
    text_test = text_test.replace(result[0],result[1])

  return text_test
