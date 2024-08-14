#!/usr/bin/env python3

"""
This module contains a single funct that inserts all documents in NoSQL
collection
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in the collection based on kwargs"""

    if mongo_collection is None:
        return []

    return mongo_collection.insert_one(kwargs).inserted_id
