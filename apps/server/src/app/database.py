"""MongoDB configuration using PyMongo."""

import os
from functools import lru_cache

from pymongo import MongoClient
from pymongo.database import Database


@lru_cache
def get_client() -> MongoClient:
    """Return a cached MongoDB client."""
    return MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))


def get_database() -> Database:
    """Return the configured application database."""
    name = os.getenv("MONGODB_DATABASE", "skills-app")
    return get_client()[name]


def ping_database() -> bool:
    """Verify that MongoDB is reachable."""
    return bool(get_client().admin.command("ping").get("ok"))
