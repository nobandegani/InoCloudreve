import httpx
import aiobotocore.session

async def b2_upload_part(
    self,
    object_key: str,
    upload_id: str,
    part_number: int,
    part_data: bytes,
    region: str | None = None,
    bucket_name: str | None = None,
    access_key_id: str | None = None,
    access_key_secret: str | None = None,
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
        region = self.b2_region

    if bucket_name is None:
        bucket_name = self.b2_bucket_name

    if access_key_id is None:
        access_key_id = self.b2_access_key_id

    if access_key_secret is None:
        access_key_secret = self.b2_access_key_secret

    session = aiobotocore.session.get_session()

    url = f'https://s3.{region}.backblazeb2.com'

    async with session.create_client(
            's3',
            region_name=region,
            endpoint_url=url,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=access_key_secret,
    ) as s3:
        try:
            await s3.upload_part(
                Bucket=bucket_name,
                Key=object_key,
                UploadId=upload_id,
                PartNumber=part_number,
                Body=part_data
            )
            return {"success": True, "status_code": 200, "msg": f"Part {part_number} uploaded"}
        except Exception as e:
            return {"success": False, "status_code": None, "msg": str(e)}
