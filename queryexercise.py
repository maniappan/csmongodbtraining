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
cursor = mcollection.find({'gid': {'$gt': 8400,'$lt': 9400}})
#-----
#cursor = mcollection.find({'$and' : [{'gid': {'$gt': 8400}},
#				 {'gid': {'$lt': 9400}}
#			 ]})
#-----
#sdate = datetime.datetime(2008,4,1)
#edate = datetime.datetime(2008,4,2)
#cursor = mcollection.find({'crdate': {'$gte': sdate, '$lt': edate}})
#-----
#sdate = datetime.datetime(2008,4,1)
#edate = datetime.datetime(2008,4,2)
#msdate = datetime.datetime(2009,1,1)
#cursor = mcollection.find({'crdate': {'$gte': sdate, '$lt': edate},'uddate': {'$gte':msdate}})
#-----
#sdate = datetime.datetime(2008,4,1)
#edate = datetime.datetime(2008,4,2)
#cursor = mcollection.find({'$and':[
#				{'crdate': {'$gte': sdate, '$lt': edate}},
#				{'langs':{'$in':['JavaScript']}}
#			]})
print cursor.count()
for c in cursor :
	print c['crdate'],c['langs']
#End
