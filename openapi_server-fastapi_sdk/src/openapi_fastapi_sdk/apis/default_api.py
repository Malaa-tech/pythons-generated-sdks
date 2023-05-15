# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_fastapi_sdk.models.extra_models import TokenModel  # noqa: F401
from openapi_fastapi_sdk.models.http_validation_error import HTTPValidationError


router = APIRouter()


@router.get(
    "/items/{item_id}",
    responses={
        200: {"model": object, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Read Item",
    response_model_by_alias=True,
)
async def get_item(
    item_id: int = Path(None, description=""),
    query_param: str = Query(None, description=""),
) -> object:
    ...
