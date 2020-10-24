from index_task import process_locaion
from db_models.models.cache_model import Cache

db_obj = Cache.objects.get(pk="5f9401947c58eb254ddf68de")

locaton_data = db_obj.image_location
print(locaton_data, "hoa")
res = process_locaion(locaton_data)
print(res)