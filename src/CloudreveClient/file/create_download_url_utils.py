
async def get_download_url(
    self,
    uri: str,
    archive: bool | None = None,
    no_cache: bool | None = None,
) -> dict:
    result = await self.create_download_url([uri], True, None, None, None, None, archive, no_cache)
    url = result["urls"][0].get("url", "") if result.get("urls") else ""
    filename = result["file_names"][0]
    extension = result["extensions"][0]
    return {
        "success": result["success"],
        "status_code": result["status_code"],
        "msg": result["msg"],
        "code": result["code"],
        "url": url,
        "file_name": filename,
        "extension": extension,
        "expires": result["expires"]
    }


