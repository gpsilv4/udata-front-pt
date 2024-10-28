"""
Romove and Renaming collections into 'geo_zone' and 'geo_level''
"""

import logging
import traceback

log = logging.getLogger(__name__)


def migrate(db):
    count = 0
    errors = 0

    log.info(
        "Removing and renaming fields from 'geo_zone' and 'geo_level' collections."
    )
    log.info("Starting the renaming process.")

    collections = ["geo_zone", "geo_level"]
    for collection_name in collections:
        if collection_name in db.list_collection_names():
            collection = getattr(db, collection_name)
            try:
                if collection_name == "geo_zone":
                    collection.update_many(
                        {},
                        {
                            "$rename": {"dbpedia": "uri"},
                            "$unset": {
                                "ancestors": "",
                                "area": "",
                                "blazon": "",
                                "flag": "",
                                "geom": "",
                                "keys": "",
                                "parents": "",
                                "population": "",
                                "successors": "",
                                "validity": "",
                                "wikipedia": "",
                            },
                        },
                    )
                else:
                    collection.update_many({}, {"$unset": {"parents": ""}})
                count += 1
            except Exception as e:
                log.error(f"An error occurred during renaming/removing: {e}")
                log.error(traceback.format_exc())
                errors += 1

    log.info("Remove and renaming process completed.")
    log.info(
        f"Successfully renamed/removed {count} collections. Encountered {errors} errors."
    )
