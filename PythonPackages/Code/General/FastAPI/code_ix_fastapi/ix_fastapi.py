from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import toml
from typing import List
import uvicorn

from modular import ix_fastapi_async


app = FastAPI()

items = [{"item_id": 1, "name": "Bar"}, {"item_id": 2, "name": "Baz"}]


class Item(BaseModel):
    item_id: int
    name: str

class Message(BaseModel):
    message: str


def check_entry_in_list(item_list, entry_id):
    entry = [i for i, j in enumerate(item_list) if j.get('item_id') == entry_id]

    if entry:
        return True
    else:
        return False


def get_entry_from_list(item_list, entry_id):
    entry = [i for i, j in enumerate(item_list) if j.get('item_id') == entry_id]
    return entry[0]


@app.get("/item/{item_id}", response_model=Item)
async def read_item(item_id: int):
    try:
        entry = get_entry_from_list(items, item_id)
        json_compatible_item_data = jsonable_encoder(items[entry])
        return JSONResponse(content=json_compatible_item_data)
    except IndexError as ie:
        raise HTTPException(status_code=406, detail=f"item with item_id {item_id} not found")


@app.get("/items", response_model=List[Item])
async def read_items():
    json_compatible_item_data = jsonable_encoder(items)
    return JSONResponse(content=json_compatible_item_data)


@app.post("/item/{item_id}/{name}", response_model=Item)
async def post_item(item_id: int, name: str):
#   check if item_id already exits
    try:
        entry_exists = check_entry_in_list(items, item_id)

        if not entry_exists:
            items.append({"item_id": item_id, "name": name})
            entry = get_entry_from_list(items, item_id)
            json_compatible_item_data = jsonable_encoder(items[entry])
            return JSONResponse(content=json_compatible_item_data)
        else:
            raise HTTPException(status_code=405, detail=f"item with item_id {item_id} already exists")

    except IndexError as ie:
        raise HTTPException(status_code=404, detail=f"item with item_id {item_id} not found")

@app.put("/item/{item_id}/{name}", response_model=Item)
async def put_item(item_id: int, name: str):
    try:
        entry = get_entry_from_list(items, item_id)
        items[entry]['name'] = name
        json_compatible_item_data = jsonable_encoder(items[entry])
        return JSONResponse(content=json_compatible_item_data)
    except IndexError as ie:
        raise HTTPException(status_code=406, detail=f"item with item_id {item_id} not found")

@app.delete("/item/{item_id}", response_model=Message)
async def delete_item(item_id: int):
    try:
        entry = get_entry_from_list(items, item_id)
        items.pop(entry)
        return {"message": f"item with item_id {item_id} deleted from items"}
    except IndexError as ie:
        raise HTTPException(status_code=406, detail=f"item with item_id {item_id} not found")


app.include_router(ix_fastapi_async.router)


if __name__ == "__main__":
    config = toml.load('./config/ix_fastapi_config.toml')
    env = config['SETUP']['env']
    host = config['PROJECT'][env]['host']
    port = config['PROJECT'][env]['port']
    protocol = config['PROJECT'][env]['protocol']

    print(f'environment set to {env}, server to {protocol}://{host}:{port}')

    uvicorn.run(app, host=host, port=port)

