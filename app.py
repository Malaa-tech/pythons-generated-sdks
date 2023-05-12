from fastapi import FastAPI
import yaml

app = FastAPI()


@app.get('/items/{item_id}')
def read_item(item_id: int, query_param: str = None):
    return {'item_id': item_id, 'query_param': query_param}


openapi_schema = app.openapi()

with open('spec.yaml', 'w') as yaml_file:
    yaml.dump(openapi_schema, yaml_file)