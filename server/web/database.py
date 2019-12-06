from . import db
from .models.submission_model import Submission
from .models.game_model import Game
from .models.environment_model import Environment

from bson.objectid import ObjectId

def insert_one(collection, document):
    return db.db[collection].insert_one(document).inserted_id

def insert_one_submission(game_id, document):
    submission_id = db.db[Submission.collection].insert_one(document).inserted_id
    
    query =  { "_id": ObjectId(game_id) }
    update = {
        "$push": { "submissions": submission_id }
    }

    db.db[Game.collection].update_one(query, update)

    return submission_id

def find_all_documents(collection, show_fields=None, hide_fields=None):
    return db.db[collection].find({}, construct_projection(show_fields, hide_fields))

def find_by_id(collection, id, show_fields=None, hide_fields=None):
    query = {
        "_id": ObjectId(id)
    }

    doc = db.db[collection].find_one(query, construct_projection(show_fields, hide_fields))

    if doc is None:
        raise Exception("Could not find an entry with that specific id.")

    return doc

def find_single_game(game_id):
    query = [
        { "$match": { "_id": ObjectId(game_id) }},
        {
            "$lookup": {
                "from" : "submissions",
                "localField" : "submissions",
                "foreignField" : "_id",
                "as" : "submissions"
            }
        }
    ]

    doc = db.db[Game.collection].aggregate(query)

    if doc is None:
        raise Exception("Could not find an entry with that specific id.")

    return doc

def find_submissions_by_game(game_id, show_fields=None, hide_fields=None):
    query = {
        "game_id": game_id
    }
    
    return db.db[Submission.collection].find(query, construct_projection(show_fields, hide_fields))
    
def find_env_by_game(game_id, show_fields=None, hide_fields=None):
    query = [
        { "$match": { "_id": ObjectId(game_id) }},
        {
            "$lookup": {
                "from" : "environments",
                "localField" : "env_id",
                "foreignField" : "_id",
                "as" : "env"
            }
        },
        { "$project": construct_projection(show_fields, hide_fields) }
    ]

    return db.db[Game.collection].aggregate(query)

def find_submissions_by_student(student_id, show_fields=None, hide_fields=None):
    query = [
        { "$match": { "group_ids": { "$elemMatch": { "$eq": student_id }}} },
        {
            "$lookup": {
                "from" : "games",
                "localField" : "game_id",
                "foreignField" : "_id",
                "as" : "game"
            }
        },
        {
            "$replaceRoot": { "newRoot": { "$mergeObjects": [ { "$arrayElemAt": [ "$game", 0 ] }, "$$ROOT" ] } }
        },
        { "$project": dict({ "game_name": "$name" }, **construct_projection(show_fields, hide_fields)) }
    ]

    return db.db[Submission.collection].aggregate(query)

def construct_projection(show_fields=None, hide_fields=None):
    if show_fields is None:
        show_fields = []
    
    if hide_fields is None:
        hide_fields = []
        
    projection = { field_name: 1 if field_name in show_fields else 0 for field_name in show_fields + hide_fields }

    if len(projection) == 0:
        projection = None

    return projection
