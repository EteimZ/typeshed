from .connection import Connection as Connection
from authlib.integrations.requests_client import OAuth2Session
from typing import Dict, List, Union
from weaviate.auth import AuthBearerToken as AuthBearerToken, AuthClientCredentials as AuthClientCredentials, AuthClientPassword as AuthClientPassword, AuthCredentials as AuthCredentials
from weaviate.exceptions import AuthenticationFailedException as AuthenticationFailedException, MissingScopeException as MissingScopeException

AUTH_DEFAULT_TIMEOUT: int
OIDC_CONFIG = Dict[str, Union[str, List[str]]]

class _Auth:
    def __init__(self, oidc_config: OIDC_CONFIG, credentials: AuthCredentials, connection: Connection) -> None: ...
    def get_auth_session(self) -> OAuth2Session: ...
