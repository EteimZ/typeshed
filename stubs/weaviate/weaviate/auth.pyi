from typing import List, Optional, Union

SCOPES = Union[str, List[str]]

class AuthClientCredentials:
    client_secret: str
    scope: Optional[SCOPES]
    scope_list: List[str]
    def __post_init__(self) -> None: ...
    def __init__(self, client_secret, scope) -> None: ...

class AuthClientPassword:
    username: str
    password: str
    scope: Optional[SCOPES]
    scope_list: List[str]
    def __post_init__(self) -> None: ...
    def __init__(self, username, password, scope) -> None: ...

class AuthBearerToken:
    access_token: str
    expires_in: int
    refresh_token: Optional[str]
    def __post_init__(self) -> None: ...
    def __init__(self, access_token, expires_in, refresh_token) -> None: ...

class AuthApiKey:
    api_key: str
    def __init__(self, api_key) -> None: ...
OidcAuth = Union[AuthBearerToken, AuthClientPassword, AuthClientCredentials]
AuthCredentials = Union[OidcAuth, AuthApiKey]
