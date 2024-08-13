#!/usr/bin/python3
"""Scrpt that list all documents in a collection"""


from typing import List 
from pymongo.collection import Collection

def list_all(mongocollection: Collection) -> List[dict]:
    """
    Args:
        mongocollection: The mongocollection object
    Returns:
        Returns a list of all documents in the collection
    """
    
    return list(mongocollection.find())

