async def download_file(
        self,
        path_to_save: str,
        uri: str,
        archive: bool | None = None,
        no_cache: bool | None = None,
):
    get_url_res = await self.get_download_url(
        uri=uri,
        archive=archive,
        no_cache=no_cache)
    if not get_url_res["success"]:
        return {
            "success": get_url_res["success"],
            "status_code": get_url_res["status_code"],
            "msg": get_url_res["msg"],
            "code": get_url_res["code"],
            "get_url_res": get_url_res
        }
    url = get_url_res["url"]
    file_name = get_url_res["file_name"]
    extension = get_url_res["extension"]

    save_file_res = await self.save_url_as_file(
        url=url,
        save_dir=path_to_save,
        filename=file_name,
        extension=extension
    )
    if not save_file_res["success"]:
        return {
            "success": save_file_res["success"],
            "status_code": save_file_res["status_code"],
            "msg": save_file_res["msg"],
            "code": save_file_res["code"],
            "get_url_res": get_url_res,
            "save_file_res": save_file_res
        }

    return {
        "success": save_file_res["success"],
        "status_code": save_file_res["status_code"],
        "msg": save_file_res["msg"],
        "code": save_file_res["code"],
        "get_url_res": get_url_res,
        "save_file_res": save_file_res,
        "url": url,
        "file_name": file_name,
        "extension": extension,
        "path": save_file_res["path"]
    }
