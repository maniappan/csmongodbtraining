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
	   " this.langs.forEach(function(z) {"
	   " emit(z,1);"
	   " });"
	   "}")

#Reduce Code
reduce = Code("function (key,values) {"
	      " var total = 0;"
	      " for (var i = 0;i<values.length;i++) {"
	      "	    total += values[i];"
	      " }"
	      " return total;"
	      "}")

#Invoke the mapreduce method
#result = mcollection.map_reduce(map,reduce,"myres")
#for doc in result.find():
#	print doc['_id'],"::",int(doc['value'])
#----------------------
#result = mcollection.aggregate([
#		{"$unwind": "$langs"},
#		{"$group": {"_id":"$langs", "count":{"$sum":1}}}
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
