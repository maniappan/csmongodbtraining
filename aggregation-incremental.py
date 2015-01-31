#!/usr/bin/python

import os
import pymongo
import datetime
from bson.code import Code

# Main Method
#Initialize Native MongoDB connection
mclient = pymongo.MongoClient('localhost',27017,w=1,j=True)
mdatabase = mclient['training']
mcollection = mdatabase['github']

#Map Code
map = Code("function(){"
	   " var s = this.size; "
	   " this.langs.forEach(function(z) {"
	   " var key = z;"
	   " var value = {count:1,size:s};"
	   " emit(key,value);"
	   " });"
	   "}")

#Reduce Code
reduce = Code("function (key,values) {"
	      " var reducedObject = {userid: key, count:0, size:0};"
	      " values.forEach(function(value) {reducedObject.count += value.count;reducedObject.size += value.size;});"
	      " return reducedObject;"
	      "}")

#Invoke the mapreduce method
#result = mcollection.map_reduce(map,reduce,"myres1")
#for doc in result.find():
#	print doc
#----------------------
#result = mcollection.aggregate([
#		{"$unwind": "$langs"},
#		{"$group": {"_id":"$langs", "count":{"$sum":1}, "size":{"$sum":"$size"}}}
#	])
#print result
#----------------------
#from bson.son import SON
#result = mcollection.aggregate([
#		{"$unwind": "$langs"},
#		{"$group": {"_id":"$langs", "count":{"$sum":1}}},
#		{"$sort": SON([("count",1),("_id",-1)])}
#	])
#print result
#End
