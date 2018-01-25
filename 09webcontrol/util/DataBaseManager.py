import pymongo

class DataBaseManager(object):
    def __init__(self):
        connection = pymongo.MongoClient() # default connect 127.0.0.1 port 27017
        tdb = connection.webControl
        self.post_info = tdb.test

    def insert(self, info):
        self.post_info.insert(info)
