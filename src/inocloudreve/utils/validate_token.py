async def validate_token(self) -> bool:
    """
    Check whether the stored access token is still valid.
    if not will refresh it
    """

    if self.is_token_valid():
        return True

    refresh_token = await self.refresh_token()
    if refresh_token["success"]:
        return True

    return False