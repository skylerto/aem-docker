import os
import pycurl
from urllib import urlencode, quote

#
# Script is used to set the replication URI.

#
publisherIp = os.environ['PUBLISHER_SERVICE_HOST']
authorUrl = 'http://' + os.environ['AUTHOR_SERVICE_HOST'] + ':4503'
password="admin:admin"

#Update Replication Agent
c = pycurl.Curl()
c.setopt(c.URL, authorUrl + "/etc/replication/agents.author/publish/jcr:content")
c.setopt(pycurl.USERPWD, password)
post_data = {'transportUri': 'http://' + publisherIp + ':4503/bin/receive?sling:authRequestLogin=1'}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.perform()

print "Checking Agent"

#Print Publisher status
c = pycurl.Curl()
c.setopt(c.URL, authorUrl + "/etc/replication/agents.author/publish/jcr:content.json")
c.setopt(pycurl.USERPWD, password)
c.perform()
