from index_web import process_url_doc
from db_models.models.web_model import Web
from create import create_collection
from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
import globals
import sys
from tsUtils.isCollectionExist import isCollectionExist
from index_task import process_index_doc

global_init()

if not isCollectionExist(globals.COLLECTION_NAME):
    print("Creating Collection")
    create_collection()

for file in Cache.objects:
    id = str(file.id)
    print(type(str(id)))
    process_index_doc.delay(id)

for site in Web.objects:
    id = str(site.id) 
    if site.text:
        # print(type(str(id)))
        process_url_doc.delay(id)
        # q.enqueue(process_url_doc, (str(id)))
