# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.5, generator: @autorest/python@6.4.12)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import FastAPISDKExampleMixinABC, _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_fast_apisdk_example_get_item_request(
    item_id: int, *, query_param: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items/{item_id}"
    path_format_arguments = {
        "item_id": _SERIALIZER.url("item_id", item_id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    if query_param is not None:
        _params["query_param"] = _SERIALIZER.query("query_param", query_param, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class FastAPISDKExampleOperationsMixin(FastAPISDKExampleMixinABC):
    @distributed_trace
    def get_item(self, item_id: int, *, query_param: Optional[str] = None, **kwargs: Any) -> Union[Any, JSON]:
        """Read Item.

        Read Item.

        :param item_id: Required.
        :type item_id: int
        :keyword query_param: Default value is None.
        :paramtype query_param: str
        :return: any or JSON object
        :rtype: any or JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 422
                response == {
                    "detail": [
                        {
                            "loc": [
                                {}
                            ],
                            "msg": "str",  # Message. Required.
                            "type": "str"  # Error Type. Required.
                        }
                    ]
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Union[Any, JSON]] = kwargs.pop("cls", None)

        request = build_fast_apisdk_example_get_item_request(
            item_id=item_id,
            query_param=query_param,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 422]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if response.status_code == 422:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if cls:
            return cls(pipeline_response, cast(Union[Any, JSON], deserialized), {})  # type: ignore

        return cast(Union[Any, JSON], deserialized)  # type: ignore
