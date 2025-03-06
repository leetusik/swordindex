import json
import os

from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def index(request):
    return render(request, "index.html")


def privacy_policy(request):
    """Render the privacy policy modal content"""
    return render(request, "modal.html")


def test_static(request):
    """Test page for static files"""
    return render(request, "test_static.html")


@csrf_exempt
@require_POST
def handle_kimchi(request):
    """Handle the kimchi API request"""
    try:
        data = json.loads(request.body)
        if data.get("keyword"):
            return JsonResponse({"response": data.get("keyword") + " kimchi"})
        return JsonResponse({"error": "Invalid keyword"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


def direct_image(request):
    """Directly serve an image file"""
    image_path = os.path.join(settings.BASE_DIR, "static", "img", "logo.png")
    if os.path.exists(image_path):
        return FileResponse(open(image_path, "rb"), content_type="image/png")
    else:
        return HttpResponse(f"Image not found at {image_path}", status=404)
