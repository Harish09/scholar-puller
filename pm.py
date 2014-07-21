import urllib2,re
from urlparse import urlparse

#http://scholar.google.com/scholar?q=+All+your+iframes+point+to+us
headers = { 'User-Agent' : 'Mozilla/5.0' }

title = "All your iframes point to us"
title_list = title.split(" ")

query = "http://scholar.google.com/scholar?q="
for item in title_list:
	query+=("+"+item)


print query

req = urllib2.Request(query, headers={ 'User-Agent': 'Mozilla/5.0' })
html = urllib2.urlopen(req).read()

match = re.search(r'http.*\.pdf', html,re.I)
if match:
	print match.group()
else:
	print "No match"
