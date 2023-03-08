import pymongo


client = pymongo.MongoClient("mongodb+srv://hegdeprashant16:hegdepkh14@clustero.pkzfguv.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['pwskills']

coll_create = db['my_record']

data = {
    
    'name' : 'prashant',
    'class':'data science',
    'timing' : 'flexi'
}

coll_create.insert_one(data)