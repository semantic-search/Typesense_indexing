from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
from init import tsClient
from task_worker.celery import celery_app
import globals

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


def process_locaion(image_location):
    try:
        location_address={}
        location_address=getVal(image_location, "location_address", {}) 
        string_index=""
        if location_address["city"]:
            string_index=image_location["location_category"]+ " "+ \
                        location_address['city'] + " " +location_address['county']+ " "\
                    +location_address['state_district']+ " "+location_address['state']+ " "+location_address['country']

        elif location_address["village"]:
            string_index = image_location["location_category"] + " "+\
                        location_address['village']+ " "+ location_address['county'] + " "\
                        + location_address['state_district'] + " "+ location_address['state'] +" "+ location_address['country']

        if image_location["location_name"]:
            print(f"in if ")
            string_index = string_index + " "+ image_location["location_name"]

        print(type(string_index), string_index)
        return string_index
    except Exception as e:
        print(f"error in process location {e}")
        return ""

@celery_app.task()
def process_index_doc(id):
    print(f"id {type(id)}")
    db_obj = Cache.objects.get(id=id)
    document = {}
    document["doc_id"] = id 
    document["file_name"] = getVal(db_obj, "file_name")
    document["mime_type"] = getVal(db_obj, "mime_type") 
    document["text"] = getVal(db_obj, "text")
    document["labels"] = getVal(db_obj, "labels", [])
    document["scores"] = getVal(db_obj, "scores", [])
    print(f"actual locaiton data",db_obj.image_location )
    image_location = process_locaion(getVal(db_obj, "image_location"))
    print(image_location, type(image_location), "ssss xxxxxxxxxxxxxxx------")
    document["image_location"] = image_location 
    document["faces"] = getVal(db_obj, "faces", [])
    document["url"]=getVal(db_obj, "url")
    document["date"] = int(getVal(db_obj, "date").strftime('%Y%m%d'))
    
    print(f"document for indexing {document}")
    res = tsClient.collections[globals.COLLECTION_NAME].documents.create(document)
    print(f"file {db_obj.file_name} indexed in typesense")
    print(res)
