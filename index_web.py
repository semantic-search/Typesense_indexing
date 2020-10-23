from db_models.mongo_setup import global_init
from db_models.models.web_model import Web
from task_worker.celery import celery_app
import globals
from init import tsClient

global_init()

def getVal(db_obj, key: str, error_res=""):
    try:
        print(type(key), "key")
        val = db_obj[key]
        if val is None:
            return error_res
        return val
    except KeyError:
        return error_res


@celery_app.task()
def process_url_doc(id):

    print(f"id {type(id)}")

    db_obj = Web.objects.get(id=id)
    document = {}
    document["doc_id"] = id
    document["text"] = getVal(db_obj, "text")
    print("THIS IS THE ID ", id)
    document["url"]=getVal(db_obj, "url")
    
    document = {}
    document["doc_id"] = id 
    document["file_name"] = getVal(db_obj, "file_name")
    document["mime_type"] = getVal(db_obj, "mime_type") 
    document["text"] = getVal(db_obj, "text")
    document["labels"] = getVal(db_obj, "labels", [])
    document["scores"] = getVal(db_obj, "scores", [])
    document["image_location"] = [] # would be always empty for web document 
    document["faces"] = getVal(db_obj, "faces", [])
    document["date"] = int(getVal(db_obj, "date").strftime('%Y%m%d'))
    document["url"]=getVal(db_obj, "url")

    res = tsClient.collections[globals.COLLECTION_NAME].documents.create(document)
    print(f"file {db_obj.file_name} indexed in typesense")
    print(res)