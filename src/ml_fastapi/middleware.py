from typing import Awaitable, Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class BearerTokenHeaderForwarding(BaseHTTPMiddleware):
    """MiddleWare that forwards a header value.
    
    MiddleWare that takes the value of a header key 
    from the incoming request and adds it to the 
    response header, effectively forwarding the authorization token.

    Args:
        auth_header_key [str]: The value of that header key gets forwarded
    """

    def __init__(self, app, auth_header_key: str):
        super().__init__(app)
        self.auth_header_key = auth_header_key

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]):
        # do something before path operation receives request
        bearer_token_header = request.headers.get(self.auth_header_key)

        response = await call_next(request)

        # do something after path operation
        if bearer_token_header is not None:
            if response is not None and response.headers is not None:
                response.headers[self.auth_header_key] = bearer_token_header

        return response
