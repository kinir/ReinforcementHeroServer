from . import db
from .models.submission_model import Submission

from bson.objectid import ObjectId

def insert_one(collection, document):
    db.db[collection].insert_one(document)

def find_all_documents(collection, show_fields=None, hide_fields=None):
    return db.db[collection].find({}, construct_projection(show_fields, hide_fields))

def find_by_id(collection, id, show_fields=None, hide_fields=None):
    query = {
        "_id": ObjectId(id)
    }

    return db.db[collection].find_one(query, construct_projection(show_fields, hide_fields))

def find_submissions_by_game(game_id, show_fields=None, hide_fields=None):
    query = {
        "game_id": game_id
    }
    
    return db.db[Submission.collection].find(query, construct_projection(show_fields, hide_fields))
    
def find_submissions_by_student(student_id, show_fields=None, hide_fields=None):
    query = {
        "group_ids": { "$elemMatch": { "$eq": student_id } }
    }

    return db.db[Submission.collection].find(query, construct_projection(show_fields, hide_fields))

def construct_projection(show_fields=None, hide_fields=None):
    if show_fields is None:
        show_fields = []
    
    if hide_fields is None:
        hide_fields = []
        
    projection = { field_name: 1 if field_name in show_fields else 0 for field_name in show_fields + hide_fields }

    if len(projection) == 0:
        projection = None

    return projection
