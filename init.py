import typesense
import globals

tsClient = typesense.Client({
  'nodes': [{
    'host': globals.TYPESENSE_HOST,
    'port': globals.TYPESENSE_PORT,
    'protocol': 'http'
  }],
  'api_key': globals.TYPESENSE_API_KEY,
  'connection_timeout_seconds': 2
})
