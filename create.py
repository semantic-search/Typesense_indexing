from init import tsClient
import globals
  
schema = {
  'name': globals.COLLECTION_NAME,
  'fields': [
    {
      'name'  :  'doc_id',
      'type'  :  'string'
    },
    {
      'name'  :  'file_name',
      'type'  :  'string'
    },
    {
      'name'  :  'mime_type',
      'type'  :  'string',
      'facet': True
    },
    {
      'name'  :  'text',
      'type'  :  'string'
    },
    {
      'name' : 'labels',
      'type' : 'string[]'
    },
    {
      'name' : 'scores',
      'type' : 'float[]'
    },
    {
      'name' : 'faces',
      'type' : 'string[]'
    },
    {
      'name'  :  'image_location',
      'type'  :  'string'
    },
    {
      'name'  :  'date',
      'type'  :  'int32'
    }
  ],
  'default_sorting_field': 'date'
}

def create_collection():
  res = tsClient.collections.create(schema)
  print(res)