import pymongo
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    try:
        client = pymongo.MongoClient('172.30.104.15',
                                    27017,
                                    username='userA24',
                                    password='uwgDyvIAgUlSjSEJ')
        db = client['sampledb']
        return "Success"
    except:
        return "Can't connect to MongoDB server with database itwonders."
        #return "Hello World!"

if __name__ == "__main__":
    application.run()
