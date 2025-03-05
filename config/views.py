from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def privacy_policy(request):
    """Render the privacy policy modal content"""
    return render(request, "modal.html")
