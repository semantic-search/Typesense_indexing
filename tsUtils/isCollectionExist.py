from init import tsClient
import typesense


def isCollectionExist(name):
    try:
        tsClient.collections[name].retrieve() 
        print(f"Collection {name} exist")
        return True
    except typesense.exceptions.ObjectNotFound:
        print(f"Collection {name} do not exist")
        return False