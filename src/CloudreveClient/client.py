import httpx

from .site import ping as _ping

from .session import password_sign_in as _password_sign_in
from .session import refresh_token as _refresh_token

from .file import get_file_info as _get_file_info
from .file import create_download_url as _create_download_url
from .file import get_download_url as _get_download_url
from .file import update_file_content as _update_file_content
from .file import list_files as _list_files

from .utils import is_token_valid as _is_token_valid
from .utils import validate_token as _validate_token
from .utils import save_url_as_file as _save_url_as_file

class CloudreveClient:
    def __init__(self, base_url: str, email: str, password: str):
        self.conn = httpx.AsyncClient(base_url=base_url.rstrip('/'))
        self.email = email
        self.password = password
        self.user_info= None
        self.token = None

    ping = _ping

    password_sign_in = _password_sign_in
    refresh_token = _refresh_token

    list_files = _list_files
    get_file_info = _get_file_info
    create_download_url = _create_download_url
    get_download_url = _get_download_url
    update_file_content = _update_file_content

    is_token_valid = _is_token_valid
    validate_token = _validate_token
    save_url_as_file = _save_url_as_file

    async def close(self):
        await self.conn.aclose()