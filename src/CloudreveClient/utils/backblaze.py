import httpx
async def b2_upload_part(
    self,
    object_key: str,
    upload_id: str,
    part_number: int,
    part_data: bytes,
    region: str | None = None,
    bucket_name: str | None = None,
) -> dict:
    """
    Upload one part of a multipart upload to Backblaze B2 via the S3-compatible API.

    Args:
        self: CloudreveClient instance
        object_key: the object’s key/path in the bucket (e.g. "Spark/test/test36.zip")
        upload_id: the multipart UploadId from create_upload_session
        part_number: which part index this is (starting at 0 or 1, per your B2 config)
        part_data: the raw bytes of this part
        region: your B2 bucket’s region (e.g. "us-west-001")
        bucket_name: the name of your B2 bucket

    Returns:
        {
            "success": bool,
            "status_code": int | None,
            "msg": str
        }
    """
    if region is None:
        region = self.region

    if bucket_name is None:
        bucket_name = self.bucket_name

    url = f"https://s3.{region}.backblazeb2.com/{bucket_name}/{object_key}"
    params = {"partNumber": part_number, "uploadId": upload_id}

    try:
        resp = await self.conn.put(url, params=params, content=part_data)
        resp.raise_for_status()
    except httpx.RequestError as exc:
        return {
            "success": False,
            "status_code": None,
            "msg": f"Upload request error: {exc}"
        }
    except httpx.HTTPStatusError as exc:
        return {
            "success": False,
            "status_code": exc.response.status_code,
            "msg": f"Upload failed with HTTP {exc.response.status_code}"
        }

    return {
        "success": True,
        "status_code": resp.status_code,
        "msg": f"Part {part_number} uploaded"
    }
