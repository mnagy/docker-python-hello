#!/usr/bin/python

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import time
import sys

class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html><body>%s</body></html>" % (time.ctime(),)

print "Running on port 1337"
sys.stdout.flush()

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(1337, factory, interface="0.0.0.0")
reactor.run()
