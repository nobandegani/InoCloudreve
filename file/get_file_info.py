import httpx

async def get_file_info(
    self,
    file: str,
    extended: bool | None = None,
    folder_summary: bool | None = None,
) -> dict:
    """
    Fetch file information from the /file/info endpoint.

    Args:
        self: CloudreveClient instance
        file: the file URI or file ID (string)
        extended: include extended metadata (bool, optional)
        folder_summary: include folder summary (bool, optional)

    Returns a dict:
        {
            "success": bool,
            "status_code": int | None,
            "msg": str,
            "code": int | None,
            "data": dict
        }
    """

    if not await self.validate_token():
        return {
            "success": False,
            "status_code": None,
            "msg": "Access token expired"
        }

    headers = {
        "Authorization": f"Bearer {self.token.get('access_token', '')}"
    }

    params = {}

    if "/" in file or "\\" in file:
        params["uri"] = "cloudreve://my/" + file
    else:
        params["id"] = file

    if extended:
        params["extended"] = extended
    if folder_summary:
        params["folder_summary"] = folder_summary

    try:
        resp = await self.conn.get("/file/info", params=params, headers=headers)
        resp.raise_for_status()
    except httpx.RequestError as exc:
        return {
            "success": False,
            "status_code": None,
            "msg": f"Request error: {exc}"
        }
    except httpx.HTTPStatusError as exc:
        return {
            "success": False,
            "status_code": exc.response.status_code,
            "msg": f"HTTP error: {exc.response.status_code}"
        }

    try:
        payload = resp.json()
    except ValueError:
        return {
            "success": False,
            "status_code": resp.status_code,
            "msg": "Invalid JSON response"
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
