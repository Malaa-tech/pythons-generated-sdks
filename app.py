from fastapi import FastAPI
import yaml

tags_metadata = [
    {
        "name": "Items SDK",
        "description":"This is the SDK for the Items API",
        "externalDocs": {
            "description": "Items SDK Docs",
            "url":"localhost:8000"
        },
    }
]

app = FastAPI(
    title="FastAPI SDK Exampleeees",
    description="This is an example of how to use the FastAPI SDK",
    version="0.1.0") # Here is the versioning

@app.get('/items/{item_id}', operation_id="GetItem")
def read_item(item_id: int, query_param: str = None):
    return {'item_id': item_id, 'query_param': query_param}

openapi_schema = app.openapi()

with open('repos/spec.yaml', 'w') as yaml_file:
    yaml.dump(openapi_schema, yaml_file)