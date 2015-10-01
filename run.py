import requests
import sys
import re

def isurl(s):
    if re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', s):
        return True
    else:
        return False

  
def getPermalink(url):
  # will need to handle cases that it can't find, like for http://w3techs.com/technologies/overview/javascript_library/all
  try:
    r = requests.get('https://web.archive.org/save/' + r)
  except:
    return url
  if r.status_code == 403:
    return url
  else:
    return 'https://web.archive.org' + r.headers['content-location']
  

text = open(sys.argv[1],'r').read()
