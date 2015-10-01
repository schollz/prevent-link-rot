# -*- coding: utf-8 -*-
import sys
import re
from multiprocessing import Pool
import requests



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
    print "Got permanent link for " + url
  except:
    return url,url
  if r.status_code == 403:
    return url,url
  else:
    try:
      return url,'https://web.archive.org' + r.headers['content-location']
    except:
      print url
      return url,url
  

def replaceText(text_test):
  urls = []
  for url in  re.findall(r'(https?://[^\s]+)', text_test):
    newurl = url.split('"')[0].split('<')[0]
    while newurl[-1] == '.' or newurl[-1] == ')' or newurl[-1] == '!':
      newurl = newurl[:-1]
    urls.append(newurl)


  p = Pool(5)
  conversion = {}
  for result in p.map(getPermalink, list(set(urls))):
    conversion[result[0]] = result[1]    
  p.terminate()

  curPos = 0
  for url in urls:
    if url in text_test[curPos:]:
      print url
      print conversion[url]
      print text_test[curPos:]
      newPos = text_test.index(url)
      text_test = text_test[0:curPos] + text_test[curPos:].replace(url,conversion[url],1)
      curPos = newPos

  return text_test


