import logging
import re

logger = logging.getLogger(__name__)


class StaticFilesDebugMiddleware:
    """
    Middleware to debug static file requests
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Compile regex to match image files
        self.image_pattern = re.compile(r"\.(png|jpg|jpeg|gif|svg)$", re.IGNORECASE)

    def __call__(self, request):
        # Check if this is a request for an image file
        if "/static/" in request.path and self.image_pattern.search(request.path):
            logger.info(f"Image request: {request.path}")
            logger.info(f"Request headers: {request.headers}")

        response = self.get_response(request)

        # Log response for image files
        if "/static/" in request.path and self.image_pattern.search(request.path):
            logger.info(f"Response status: {response.status_code}")
            logger.info(f"Response headers: {response.headers}")

        return response
