import os

from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def privacy_policy(request):
    """Render the privacy policy modal content"""
    return render(request, "modal.html")


def test_static(request):
    """Test page for static files"""
    return render(request, "test_static.html")


def direct_image(request):
    """Directly serve an image file"""
    image_path = os.path.join(settings.BASE_DIR, "static", "img", "logo.png")
    if os.path.exists(image_path):
        return FileResponse(open(image_path, "rb"), content_type="image/png")
    else:
        return HttpResponse(f"Image not found at {image_path}", status=404)
