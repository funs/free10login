# -*- coding: utf-8 -*-

import urllib
import urllib2

#uri = 'https://www.google.com.tw/'
uri = 'http://free10.com.tw/10/proc_ex.php?cmd=validate&randomkey=498318&language=tw'

request = urllib2.Request(uri)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
request.add_header('X-Requested-With','XMLHttpRequest')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0')
#request.add_header('Referer','http://free10.com.tw/10/hotspotlogin.php?res=logoff&uamip=192.168.182.1&uamport=3990&challenge=1f31f330bead472d530775092a991dfa&userurl=&nasid=B0-C7-45-6E-27-37&mac=00-D0-41-C3-31-E6')

values = {'msisdn':'0911220970','telco':'cht','billing':'3000','code':'0956',
          'mac':'00-D0-41-C3-31-E6','nasid':'B0-C7-45-6E-27-37','chal':'1a8f3aa25140949b9a9803f1fbb41701',
          'uamip':'192.168.182.1','uamport':'3990','userurl':''}

data = urllib.urlencode(values)
response = urllib2.urlopen(request,data)

#redirected = response.geturl()==uri
#print(redirected)

html = response.read()
#json.loads(jsonText)
print(html)