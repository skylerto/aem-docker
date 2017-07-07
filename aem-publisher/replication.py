import os
import pycurl
# from urllib import urlencode, quote
try:
    from urllib import urlencode, quote
except ImportError:
    from urllib.parse import urlencode, quote

#
# Script is used to set the replication URI.

#
publisherIp = os.environ['PUBLISHER_IP']
# publisherIp = '10.0.0.174'
authorUrl = 'http://' + os.environ['AUTHOR_BASE']
# authorUrl = 'http://192.168.99.100:32394'
password="admin:admin"

title = publisherIp.replace('.', '-')

# create a new replication agent
# curl -u admin:admin  -H 'Content-Type: application/x-www-form-urlencoded;
# charset=UTF-8' --data

c = pycurl.Curl()
c.setopt(c.URL, authorUrl + "/bin/wcmcommand")
c.setopt(pycurl.USERPWD, password)
# post_data = { data }
# Form data must be provided already urlencoded.
# postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
data = 'cmd=createPage&_charset_=utf-8&parentPath=/etc/replication/agents.author&title=' + title + '&label=&template=/libs/cq/replication/templates/agent'
c.setopt(c.POSTFIELDS, data)
c.perform()



# #Update Replication Agent
c = pycurl.Curl()
c.setopt(c.URL, authorUrl + "/etc/replication/agents.author/" + title + "/jcr:content")
c.setopt(pycurl.USERPWD, password)
post_data = {
        'transportUri': 'http://' + publisherIp + ':4503/bin/receive?sling:authRequestLogin=1',
        'transportUser':'admin',
        'transportPassword':'{DES}8aadb625ced91ac483390ebc10640cdf',
        'enabled': 'true'
}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.perform()

# print "Checking Agent"

# #Print Publisher status
c = pycurl.Curl()
c.setopt(c.URL, authorUrl + "/etc/replication/agents.author/" + title + "/jcr:content.json")
c.setopt(pycurl.USERPWD, password)
c.perform()
