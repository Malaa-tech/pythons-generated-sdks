import typing_extensions

from fastapi_sdk.paths import PathValues
from fastapi_sdk.apis.paths.items_item_id import ItemsItemId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ITEMS_ITEM_ID: ItemsItemId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ITEMS_ITEM_ID: ItemsItemId,
    }
)
