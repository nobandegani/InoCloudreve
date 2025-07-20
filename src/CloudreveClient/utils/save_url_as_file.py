import os
import httpx

async def save_url_as_file(
    self,
    url: str,
    save_dir: str,
    filename: str,
    extension: str
) -> dict:
    """
    Download a file from `url` and save it to `save_dir/filename+extension`.

    Args:
        self: CloudreveClient instance
        url: the download URL (string)
        save_dir: directory path to save the file (string)
        filename: base name for the saved file (string)
        extension: file extension including the dot, e.g. ".zip" or ".png" (string)

    Returns:
        {
            "success": bool,
            "status_code": int | None,
            "msg": str,
            "code": int | None,
            "path": str  # full path to the saved file
        }
    """

    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{filename}{extension}")

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            resp.raise_for_status()
    except httpx.RequestError as exc:
        return {
            "success": False,
            "status_code": None,
            "msg": f"Request error: {exc}",
            "code": None,
            "path": ""
        }
    except httpx.HTTPStatusError as exc:
        return {
            "success": False,
            "status_code": exc.response.status_code,
            "msg": f"HTTP error: {exc.response.status_code}",
            "code": exc.response.status_code,
            "path": ""
        }

    try:
        with open(file_path, "wb") as f:
            f.write(resp.content)
    except OSError as exc:
        return {
            "success": False,
            "status_code": resp.status_code,
            "msg": f"File write error: {exc}",
            "code": resp.status_code,
            "path": ""
        }

    return {
        "success": True,
        "status_code": resp.status_code,
        "msg": "",
        "code": resp.status_code,
        "path": file_path
    }
