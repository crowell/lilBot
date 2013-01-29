import praw
import urllib2
import urllib
import time
import string
import sys
from BeautifulSoup import *


user_agent = 'Lil\' B for Lil\' Bot EVIL EDITION'
headers = {'User-Agent' : user_agent}

req = urllib2.Request("http://music.furstlabs.com/queue", '', headers)
resp = urllib2.urlopen(req)
page = resp.read()
pool = BeautifulSoup(page)

toDelete = []

res = pool.findAll('tr')
for result in res:
    toDelete.append(result['id'])

for ii in toDelete:
    print ii

for ii in range(500,100000):
    url = 'http://music.furstlabs.com/queue'
    user_agent = 'Lil\' B for Lil\' Bot'
    header = { 'User-Agent' : user_agent }
    values = { 'change' : 'remove',
            'removed': ii}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, header)
    print urllib2.urlopen(req)
