import os
from pymongo import MongoClient

MONGODB_URL = os.environ.get('MONGODB_URL')
if not MONGODB_URL:
    raise ValueError('MONGODB_URL environment variable not set')

client = MongoClient(MONGODB_URL)
db = client.get_database()
users_collection = db.get_collection('users')


def add_user(user_id, user_name):
    user = {'_id': user_id, 'name': user_name}
    result = users_collection.insert_one(user)
    return result.inserted_id


def get_user(user_id):
    user = users_collection.find_one({'_id': user_id})
    return user


def remove_user(user_id):
    result = users_collection.delete_one({'_id': user_id})
    return result.deleted_count
