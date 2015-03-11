#!/usr/bin/env python2.6
from datetime import datetime
import calendar
import time

dt1 = datetime.utcnow()
print "UTC Now"
print dt1

print "Unix timestamp GM/UTC time"
print calendar.timegm(dt1.utctimetuple())

print "Unix timestamp Localtime"
print time.mktime(dt1.utctimetuple())

print "Convert unix timestamp (utc) to datetime UTC/GM time"
print datetime.utcfromtimestamp( calendar.timegm(dt1.utctimetuple())   )

print "Convert unix timestamp (local) to datetime UTC/GM time"
print datetime.utcfromtimestamp( time.mktime(dt1.utctimetuple())   )
print "Convert unix timestamp (utc) to datetime local"
print time.localtime( calendar.timegm(dt1.utctimetuple()) )


print "-------------------"
dt1 = datetime(2014, 3, 24)
dt2 = datetime(2014, 3, 25)

print "Unix timestamp Localtime"
print time.mktime(dt1.utctimetuple())
print time.mktime(dt2.utctimetuple())


