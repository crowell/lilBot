import praw
import urllib2
import urllib
import time
import string
import sys
from BeautifulSoup import *


print "Lil\' B for Lil\' Bot - Dequeue : Evil Edition'

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

for ii in reversed(toDelete):
    url = 'http://music.furstlabs.com/queue'
    header = { 'User-Agent' : user_agent }
    values = { 'change' : 'remove',
            'removed': ii}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, header)
    urllib2.urlopen(req)

print "ALL DONE!"
