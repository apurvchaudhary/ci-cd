from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['ci_cd_db']
pipelines_collection = db['pipelines']
jobs_collection = db['jobs']