#!/usr/bin/python3
"""Script that list all documents in a collection"""
from typing import List 
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Args:
        mongocollection: The mongocollection object
    Returns:
        Returns a list of all documents in the collection
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find({}))

