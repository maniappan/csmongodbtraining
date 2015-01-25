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

#Open the data file and start the datainserts
for line in open('github-2009',"r"):
    line = line.strip('\n')
    fields = line.split('|')
    projid_str = fields[0]
    proj_name_str = fields[1]
    fork_str = fields[2]
    desc_str = fields[3]
    create_date_str = fields[4]
    lstupd_date_str = fields[5]
    size_str = fields[6]
    subscnt_str = fields[7]
    wtchcnt_str = fields[8]
    isscnt_str = fields[9]
    langs_str = fields[10]
    langs_arr = []
    larr = langs_str.split(',')
    for l in larr:
	langs_arr.append(l)

    create_date = ""
    updt_date = ""
    if(create_date_str!=""):
        create_date = formatdate(create_date_str)
    if(lstupd_date_str!=""):
        updt_date = formatdate(lstupd_date_str)

    if(size_str==""):
        size_str='0'
    if(subscnt_str==""):
        subscnt_str = '0'
    if(wtchcnt_str==""):
        wtchcnt_str = '0'
    if(isscnt_str==""):
        isscnt_str = '0'

    entry = {'gid':int(projid_str),
         'name':proj_name_str,
         'desc':desc_str,
         'fork':fork_str,
         'crdate':create_date,
         'uddate':updt_date,
         'size':int(size_str),
         'subs':int(subscnt_str),
         'wtch':int(wtchcnt_str),
         'isus':int(isscnt_str),
         #'langs':langs_str
         'langs':langs_arr
    }

# Insert into MongoDB 
    in_time1 = datetime.datetime.now()
    miid = mcollection.insert(entry)
    print 'MI: %s, id : %s, MO:%s' % (in_time1, projid_str, datetime.datetime.now())

#End
