import init
import globals

res = init.tsClient.collections[globals.COLLECTION_NAME].delete()
print(res)
