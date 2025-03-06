import logging

logger = logging.getLogger(__name__)


class StaticFilesDebugMiddleware:
    """
    Middleware to debug static file requests - kept as a placeholder.
    This middleware is no longer needed but kept as a stub to avoid import errors.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
