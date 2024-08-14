#!/usr/bin/env python3 
"""code with a class to """

import redis
import uuid
from typing import Union

class Cache:
    """
    Redis caching 
    """
    def __init__(self) -> None:
        """init function for the cache class
        args:
            self
        returns: None
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Function that stores key and the data inputed 
        args:
            self, data
        returns:
            The id of data set
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
