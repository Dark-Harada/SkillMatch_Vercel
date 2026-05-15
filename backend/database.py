from pymongo import MongoClient

MONGO_URL = "mongodb+srv://thomazwaichel:481292481292@skillmatch.lit8kjo.mongodb.net/?appName=SkillMatch"

client = MongoClient(MONGO_URL)
db = client["skillmatch"]
players_collection = db["players"]
