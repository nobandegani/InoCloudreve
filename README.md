# Cloudreve Python Client

An **async** Python client for the [Cloudreve API](https://github.com/cloudreve/).  
Supports authentication, file operations, token management, and utilities—built on [httpx](https://www.python-httpx.org/) and [aiofiles](https://github.com/Tinche/aiofiles).

---

## Important Note
> **Active Development**  
> This client library is under active development and is not yet feature-complete. It was built to satisfy specific use-cases and may change without warning.
>
> **Not Production-Ready**  
> Use at your own risk. Do **not** deploy this in production environments unless you fully understand its internals and have thoroughly tested it for your needs.
>
> Contributions, feedback, and issue reports are welcome—but please be cautious if you plan to rely on this library for critical workloads.
---
## Features

- **Health check** (`ping`)  
- **Authentication**  
  - `password_sign_in(email, password, ...)`  
  - `refresh_token(token)`  
  - `is_token_valid()` / `validate_token()`  
- **File operations**  
  - `list_files(uri, page, page_size, …)`  
  - `get_file_info(file_uri, file_id, …)`  
  - `get_download_url(uris, download, archive, …)`  
  - `update_file_content(file_uri, content, previous)`  
- **Download & save**  
  - `save_url_as_file(url, save_dir, filename, extension, overwrite)`  
- **Utilities**  
  - `read_file_as_bytes(path)`

---

## Installation

```bash
# Install from PyPI
pip install InoCloudreve

# install locally:
git clone https://github.com/nobandegani/InoCloudreve.git
cd InoCloudreve
pip install -e .
```
---

## License
Mozilla Public License Version 2.0