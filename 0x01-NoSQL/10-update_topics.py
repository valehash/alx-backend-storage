#!/usr/bin/env python3

"""
This module contains a single funct that inserts all documents in NoSQL
collection
"""


def update_topics(mongo_collection, name, topics):
    """updates all topics in the schoool based on the name"""

    if mongo_collection is None:
        return []
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
