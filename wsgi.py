import pymongo
from flask import Flask
application = Flask(__name__)

try:
    client = pymongo.MongoClient('172.30.104.15',
                                27017,
                                username='userA24',
                                password='uwgDyvIAgUlSjSEJ')
    db = client['sampledb']
except:
    print("Can't connect to MongoDB server with database itwonders.")

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
