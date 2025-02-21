import subprocess
from typing import Dict, Optional
from weaviate import exceptions as exceptions
from weaviate.exceptions import WeaviateStartUpError as WeaviateStartUpError

DEFAULT_BINARY_PATH: str
DEFAULT_PERSISTENCE_DATA_PATH: str
GITHUB_RELEASE_DOWNLOAD_URL: str

class EmbeddedOptions:
    persistence_data_path: str
    binary_path: str
    version: str
    port: int
    hostname: str
    additional_env_vars: Optional[Dict[str, str]]
    def __init__(self, persistence_data_path, binary_path, version, port, hostname, additional_env_vars) -> None: ...

def get_random_port() -> int: ...

class EmbeddedDB:
    data_bind_port: int
    options: EmbeddedOptions
    process: Optional[subprocess.Popen[bytes]] = None
    def __init__(self, options: EmbeddedOptions) -> None: ...
    def __del__(self) -> None: ...
    def ensure_paths_exist(self) -> None: ...
    def ensure_weaviate_binary_exists(self) -> None: ...
    def is_listening(self) -> bool: ...
    def wait_till_listening(self) -> None: ...
    @staticmethod
    def check_supported_platform() -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def ensure_running(self) -> None: ...
