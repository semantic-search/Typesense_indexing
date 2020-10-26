from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import globals

from init import tsClient

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/typesense/{item}")
async def search_item(item: str):

    search_parameters = {
    'q'         : item,
    'query_by'  : 'text, file_name, labels, image_location, mime_type, doc_id',
    'facet_by' : 'mime_type',
    'per_page' : 20
    }  

    result = tsClient.collections[globals.COLLECTION_NAME].documents.search(search_parameters)

    return result