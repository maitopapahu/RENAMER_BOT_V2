import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","Cluster0")
DB_URL = os.environ.get("DB_URL","mongodb+srv://newuser:<newuser>@cluster0.0fs6z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None , "date":0}
            try:
            	dbcol.insert_one(user_det)
            except:
            	value = 'new'
            	return value
            	pass

def addthumb(chat_id, file_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":file_id}})
	
def delthumb(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":None}})
	
def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             lgcd = i["file_id"]
             return lgcd 

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
    
def find_one(id):
	return dbcol.find_one({"_id":id})
