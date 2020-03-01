# encoding: utf-8
# Author    : AP
# Datetime  : 2019/9/6 11:05
# Project   : RBAC
import pymongo
from bson import ObjectId

#
# col = pymongo.MongoClient("mongodb://192.168.0.199:27017").get_database('test').get_collection('test')
# # col.insert_one({"1": "123123", "2": "234234", "3": "345345"})
# fuzzy_search = {"$or": [{"1": {"$regex": ".*3.*"}}, {"2": {"$regex": ".*2.*"}}],"$and":[{"1": {"$regex": ".*3.*"}}, {"2": {"$regex": ".*2.*"}}]}
# print(list(col.find(fuzzy_search)))
print("123".isdigit())
t = [{"1": 1}, {"1": 2}]
for i in t:
	i["1"] = 3
print(t)
