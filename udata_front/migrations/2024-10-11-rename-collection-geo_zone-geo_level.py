"""
Renaming collection from 'geo_zone' to 'GeoZone' and 'geo_level' to 'GeoLevel'
"""

import logging
from mongoengine.connection import connect, get_db

log = logging.getLogger(__name__)

def connect_to_mongo():
    connect('udata', host='localhost', port=27017)

def migrate():
    log.info("Renaming collection from 'geo_zone' to 'GeoZone'.")
    
    # Connects to the database
    db = get_db()

    # Checks if the ‘geo_zone’ collection exists
    if 'geo_zone' in db.list_collection_names():
       # Renew the collection
       db.geo_zone.rename('GeoZone')
       log.info("Rename successfully completed.")
    else:
       log.error("The ‘geo_zone’ collection does not exist in the database.")
    
    # Checks if the geo_level collection exists
    if 'geo_level' in db.list_collection_names():
       # Renew the collection
       db.geo_level.rename('GeoLevel')
       log.info("Rename successfully completed.")
    else:
       log.error("The geo_level collection does not exist in the database.")

if __name__ == "__main__":
    connect_to_mongo() 
    migrate()