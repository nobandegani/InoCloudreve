import httpx

async def list_files(
    self,
    uri: str,
    page: int = 0,
    page_size: int = 50,
    order_by: str | None = None,
    order_direction: str | None = None,
    next_page_token: str | None = None,
) -> dict:
    """
    List files via GET /file.

    Args:
        self: CloudreveClient instance
        uri: the directory URI (string)
        page: page index (integer, default 0)
        page_size: number of items per page (integer, default 50)
        order_by: field to order by (string, default "created_at")
        order_direction: sort direction ("asc" or "desc", default "asc")
        next_page_token: cursor for next page (string, optional)

    Returns:
        {
            "success": bool,
            "status_code": int | None,
            "msg": str,
            "code": int | None,
            "data": dict  # contains files list, parent, pagination, etc.
        }
    """

    if not await self.validate_token():
        return {
            "success": False,
            "status_code": None,
            "msg": "Access token expired",
            "code": None,
            "data": {},
        }

    params = {
        "uri": "cloudreve://my/" + uri,
        "page": page,
        "page_size": page_size
    }

    if order_by:
        params["order_by"] = order_by

    if order_direction:
        params["order_direction"] = order_direction

    if next_page_token:
        params["next_page_token"] = next_page_token

    try:
        resp = await self.conn.get("/file", params=params, headers=self.get_headers(True, False))
        resp.raise_for_status()
    except httpx.RequestError as exc:
        return {
            "success": False,
            "status_code": None,
            "msg": f"Request error: {exc}",
            "code": None,
            "data": {},
        }
    except httpx.HTTPStatusError as exc:
        return {
            "success": False,
            "status_code": exc.response.status_code,
            "msg": f"HTTP error: {exc.response.status_code}",
            "code": None,
            "data": {},
        }

    try:
        payload = resp.json()
    except ValueError:
        return {
            "success": False,
            "status_code": resp.status_code,
            "msg": "Invalid JSON response",
            "code": None,
            "data": {},
        }

    code = payload.get("code", -1)
    data = payload.get("data", {})

    # 5) Return structured result
    return {
        "success": code == 0,
        "status_code": resp.status_code,
        "msg": payload.get("msg", ""),
        "code": code,
        "data": data,
    }
