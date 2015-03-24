# -*- coding: utf-8 -*-

import urllib
import urllib2
from urlparse import urlparse, parse_qs

#uri = 'http://free10.com.tw/10/hotspotlogin.php?res=success&uamip=192.168.182.1&uamport=3990&uid=0911220979&userurl=http://www.google.com.tw&nasid=B0-C7-45-6E-27-37&mac=00-D0-41-C3-31-E6#page_welcome'
#uri = 'https://www.facebook.com/holinetw'
#uri = 'http://www.google.com.tw'
uri = 'http://free10.com.tw/10/hotspotlogin.php?res=notyet&uamip=192.168.182.1&uamport=3990&challenge=997b2c88b8a105922bd8c0e190e45e08&userurl=http%3a%2f%2fwww.google.com.tw%2f&nasid=B0-C7-45-6E-27-37&mac=00-D0-41-C3-31-E6'
request = urllib2.Request(uri)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
request.add_header('X-Requested-With','XMLHttpRequest')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0')
#request.add_header('Referer','http://free10.com.tw/10/hotspotlogin.php?res=logoff&uamip=192.168.182.1&uamport=3990&challenge=1f31f330bead472d530775092a991dfa&userurl=&nasid=B0-C7-45-6E-27-37&mac=00-D0-41-C3-31-E6')

response = urllib2.urlopen(request)

redirected = response.geturl()==uri
print(redirected)
html = response.read()
print(response.geturl())

