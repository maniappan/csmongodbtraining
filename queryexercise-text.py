#!/usr/bin/python

import os
import pymongo
import datetime

# Methods
def formatdate(date_str):
    date_arr=""
    vsplit = date_str.split('T')
    dsplit = vsplit[0].split("-")
    tsplit = vsplit[1].split(':')

    y = int(dsplit[0])
    m = int(dsplit[1])
    d = int(dsplit[2])
    h = int(tsplit[0][1:])
    mt = int(tsplit[1])
    s = int(tsplit[2][:-1])
    d = datetime.datetime(y,m,d,h,mt,s)
    #print d
    return d

# Main Method
#Initialize Native MongoDB connection
mclient = pymongo.MongoClient('localhost',27017,w=1,j=True)
mdatabase = mclient['training']
mcollection = mdatabase['github']

#-----
# Steps for text search
# Start mongod with --setParameter textSearchEnabed=true
# Run db.<collection>.ensureIndex({<key> :"text"})
#
cursor = mcollection.find({'$text': {'$search': 'Tivo'}})
print cursor.count()
for c in cursor :
	print c['crdate'],c['desc']
#End
