from pathlib import Path
from os import path, environ

import pytest

root = Path.cwd()
if not environ.get("APP_ENV") or environ.get("APP_ENV") == "local":
    from dotenv import load_dotenv

    dot_env_path = path.join(str(root), "local.env")
    load_dotenv(dot_env_path)


@pytest.fixture(scope="session")
def api_address():
    return f"http://{environ.get('SERVER_LOCALHOST')}:{environ.get('API_PORT')}"
