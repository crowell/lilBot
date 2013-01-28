import praw
import urllib2
import urllib
import time
r = praw.Reddit('Lil\' B for Lil\' Bot')
mini = 0
while True:
    listing = r.get_subreddit('thankyoubasedgod').get_new_by_date()
    first = True
    tmpmin = 0
    for item in listing:
        if first == True:
            tmpmin = item.created
            first = False
        link = item.url
        if "youtube" not in link:
            if "youtu.be" not in link:
                if "vimio" not in link:
                    if "soundcloud" not in link:
                        if "bandcamp" not in link:
                            continue
        if item.created <= mini:
            continue
        url = 'http://music.furstlabs.com/submit'
        user_agent = 'Lil\' B for Lil\' Bot'
        header = { 'User-Agent' : user_agent }
        values = { 'uri' : link }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data, header)
        urllib2.urlopen(req)
    mini = tmpmin
    time.sleep(1800) #1/2 hour
