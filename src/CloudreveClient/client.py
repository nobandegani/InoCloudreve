import httpx

from .site import ping as _ping

from .session import password_sign_in as _password_sign_in
from .session import refresh_token as _refresh_token
from .session import generate_token as _generate_token
from .session import decode_token as _decode_token

from .file import get_file_info as _get_file_info
from .file import create_download_url as _create_download_url
from .file import get_download_url as _get_download_url
from .file import update_file_content as _update_file_content
from .file import list_files as _list_files
from .file import create_upload_session as _create_upload_session
from .file import delete_upload_session as _delete_upload_session
from .file import delete_file as _delete_file
from .file import force_unlock as _force_unlock
from .file import get_last_folder_or_file as _get_last_folder_or_file

from .utils import is_token_valid as _is_token_valid
from .utils import validate_token as _validate_token
from .utils import save_url_as_file as _save_url_as_file
from .utils import read_file_as_bytes as _read_file_as_bytes
from .utils import get_headers as _get_headers

class CloudreveClient:
    def __init__(self):
        self.base_url = None
        self.conn = None
        self.email = None
        self.password = None
        self.user_info= None
        self.token = None

    def init(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.conn = httpx.AsyncClient(base_url=self.base_url)

    ping = _ping

    password_sign_in = _password_sign_in
    refresh_token = _refresh_token
    generate_token = _generate_token
    decode_token = _decode_token

    list_files = _list_files
    get_file_info = _get_file_info
    create_download_url = _create_download_url
    get_download_url = _get_download_url
    update_file_content = _update_file_content
    create_upload_session = _create_upload_session
    delete_upload_session = _delete_upload_session
    delete_file = _delete_file
    force_unlock = _force_unlock
    get_last_folder_or_file = _get_last_folder_or_file

    is_token_valid = _is_token_valid
    validate_token = _validate_token
    save_url_as_file = _save_url_as_file
    read_file_as_bytes = _read_file_as_bytes
    get_headers = _get_headers

    async def close(self):
        await self.conn.aclose()