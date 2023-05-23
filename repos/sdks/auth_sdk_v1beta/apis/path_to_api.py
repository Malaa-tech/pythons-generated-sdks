import typing_extensions

from auth_sdk_v1beta.paths import PathValues
from auth_sdk_v1beta.apis.paths.items_item_id import ItemsItemId

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
