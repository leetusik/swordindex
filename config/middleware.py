import logging
import os
import re

from django.conf import settings

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

            # Check if the file exists in the static directory
            relative_path = request.path.replace("/static/", "")
            static_path = os.path.join(settings.STATIC_ROOT, relative_path)

            if os.path.exists(static_path):
                logger.info(f"Image file exists at: {static_path}")
                logger.info(f"File size: {os.path.getsize(static_path)} bytes")
                logger.info(
                    f"File permissions: {oct(os.stat(static_path).st_mode)[-3:]}"
                )
            else:
                logger.warning(f"Image file NOT found at: {static_path}")
                # Check if it exists in the development static directories
                for static_dir in settings.STATICFILES_DIRS:
                    alt_path = os.path.join(static_dir, relative_path)
                    if os.path.exists(alt_path):
                        logger.info(f"Image file found in dev static dir: {alt_path}")

        response = self.get_response(request)

        # Log response for image files
        if "/static/" in request.path and self.image_pattern.search(request.path):
            logger.info(f"Response status: {response.status_code}")
            logger.info(f"Response headers: {response.headers}")
            if response.status_code != 200:
                logger.warning(
                    f"Failed to serve image: {request.path} (Status: {response.status_code})"
                )

        return response
