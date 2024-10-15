"""
Renaming collection from 'geo_zone' to 'GeoZone' and 'geo_level' to 'GeoLevel'
"""

import logging
import traceback

log = logging.getLogger(__name__)

def migrate(db):
    """Rename collections in the MongoDB database."""
    count = 0
    errors = 0
    
    log.info("Starting the renaming process.")

    try:
        # Rename 'geo_zone' to 'GeoZone'
        if 'geo_zone' in db.list_collection_names():
            db.geo_zone.rename('GeoZone')
            log.info("Renamed collection 'geo_zone' to 'GeoZone'.")
            count += 1
        else:
            log.warning("'geo_zone' collection does not exist.")

        # Rename 'geo_level' to 'GeoLevel'
        if 'geo_level' in db.list_collection_names():
            db.geo_level.rename('GeoLevel')
            log.info("Renamed collection 'geo_level' to 'GeoLevel'.")
            count += 1
        else:
            log.warning("'geo_level' collection does not exist.")
    except Exception as e:
        log.error(f"An error occurred during renaming: {e}")
        log.error(traceback.format_exc())
        errors += 1

    log.info("Renaming process completed.")
    log.info(f"Successfully renamed {count} collections. Encountered {errors} errors.")