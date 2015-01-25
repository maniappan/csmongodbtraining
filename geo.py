#!/usr/bin/python

import os
import pymongo
import datetime

# Main Method
#Initialize Native MongoDB connection
mclient = pymongo.MongoClient('localhost',27017,w=1,j=True)
mdatabase = mclient['geo']
airports = mdatabase['airports']
states = mdatabase['states']

cal = states.find_one({'code':'CA'});
#print cal
result = airports.find(
	   {
	   'loc': {'$geoWithin':{'$geometry': cal['loc']}}
	   },
	   { '$name' : 0 }	
	 )
for r in result:
	print r['name']
#End
