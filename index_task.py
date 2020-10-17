from init import tsClient
from task_worker.celery import celery_app
import globals

def getVal(db_obj, key: str, error_res=""):
    try:
        val = db_obj[key]
        return val
    except KeyError:
        return error_res

@celery_app.task()
def process_index_doc(db_obj):
    document = {}
    document["doc_id"] = getVal(db_obj, "id")
    document["file_name"] = getVal(db_obj, "file_name")
    document["mime_type"] = getVal(db_obj, "mime_type") 
    document["text"] = getVal(db_obj, "text")
    document["labels"] = getVal(db_obj, "labels", [])
    document["scores"] = getVal(db_obj, "scores", [])
    document["image_location"] = getVal(db_obj, "image_location", [])

    document["date"] = int(getVal(db_obj, "date").strftime('%Y%m%d'))
    
    res = tsClient.collections[globals.COLLECTION_NAME].documents.create(document)
    print(f"file {db_obj.file_name} indexed in typesense")
    print(res)

