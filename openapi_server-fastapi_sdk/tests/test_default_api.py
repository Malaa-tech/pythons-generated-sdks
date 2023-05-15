# coding: utf-8

from fastapi.testclient import TestClient


from openapi_fastapi_sdk.models.http_validation_error import HTTPValidationError  # noqa: F401


def test_get_item(client: TestClient):
    """Test case for get_item

    Read Item
    """
    params = [("query_param", 'query_param_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/items/{item_id}".format(item_id=56),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

