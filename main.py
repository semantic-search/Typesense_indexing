from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
import globals
import sys
from tsUtils.isCollectionExist import isCollectionExist
from index_task import process_index_doc

global_init()

if not isCollectionExist(globals.COLLECTION_NAME):
    print("Exiting Script")
    sys.exit()

for file in Cache.objects[:5]:
    id = file.id
    process_index_doc.delay(id)
