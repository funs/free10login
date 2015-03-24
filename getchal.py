# -*- coding: utf-8 -*-

import urllib
import urllib2
from urlparse import urlparse, parse_qs

uri = 'http://www.google.com.tw/'

request = urllib2.Request(uri)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
request.add_header('X-Requested-With','XMLHttpRequest')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0')
#request.add_header('Referer','http://free10.com.tw/10/hotspotlogin.php?res=logoff&uamip=192.168.182.1&uamport=3990&challenge=1f31f330bead472d530775092a991dfa&userurl=&nasid=B0-C7-45-6E-27-37&mac=00-D0-41-C3-31-E6')

response = urllib2.urlopen(request)

redirected = response.geturl()==uri
print(redirected)
o = parse_qs(urlparse(response.geturl()).query)
print(o['challenge'][0])
html = response.read()

