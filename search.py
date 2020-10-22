from init import tsClient
import json
import globals

search_parameters = {
  'q'         : 'the',
  'query_by'  : 'text',
  'facet_by' : 'mime_type'
}

result = tsClient.collections[globals.COLLECTION_NAME].documents.search(search_parameters)

json_object = json.dumps(result, indent = 4) 
with open("res.json", "w") as outfile: 
    outfile.write(json_object) 

#---------------------------------------------------------------------------------------------------------

# search_parameters = {
#   'q'         : 'sark',
#   'query_by'  : 'company_name',
#   'filter_by' : 'num_employees:>100',
#   'sort_by'   : 'num_employees:desc'
# }

# res = client.collections['companies'].documents.search(search_parameters)
# print(res)