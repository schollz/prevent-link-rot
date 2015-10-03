# -*- coding: utf-8 -*-
import sys
import re
import json
from multiprocessing import Pool, cpu_count

import requests

from settings import *



def isurl(s):
    if re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', s):
        return True
    else:
        return False

  
def getWebArchiveLink(url):
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
    
def getPermaccLink(dat):
  # will need to handle cases that it can't find, like for http://w3techs.com/technologies/overview/javascript_library/all
  url = dat[0]
  apikey = dat[1]
  payload = {'url': url, 'title': url}
  permacc_url =  'https://api.perma.cc/v1/archives/?api_key=' + apikey
  r = requests.post(permacc_url, data = json.dumps(payload))
  print r.status_code
  if r.status_code == 201:
    result = json.loads(r.text)
    print json.dumps(result,indent=4)
    return url,str('http://perma.cc/' + result['guid'])
  else:
    return url,url
  

def replaceText(text_test,apikey):
  urls = []
  urls_in_order = []
  for url in  re.findall(r'(https?://[^\s]+)', text_test):
    newurl = url.split('"')[0].split('<')[0]
    while newurl[-1] == '.' or newurl[-1] == ')' or newurl[-1] == '!':
      newurl = newurl[:-1]
    if not apikey:
      urls.append(newurl)
    else:
      urls.append((newurl,apikey))
    urls_in_order.append(newurl)


  f = getWebArchiveLink
  if apikey:
    f = getPermaccLink
  p = Pool(cpu_count())
  conversion = {}
  for result in p.map(f, list(set(urls))):
    conversion[result[0]] = result[1]    
  p.terminate()

  print conversion
  curPos = 0
  for url in urls_in_order:
    if url in text_test[curPos:]:
      print url
      print conversion[url]
      print text_test[curPos:]
      newPos = text_test.index(url)
      text_test = text_test[0:curPos] + text_test[curPos:].replace(url,conversion[url],1)
      curPos = newPos

  return text_test  



