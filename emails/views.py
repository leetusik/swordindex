from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import WaitlistEmail

# Create your views here.


def collect_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        try:
            WaitlistEmail.objects.create(email=email)
            return JsonResponse(
                {"message": "Email successfully added to waitlist"}, status=200
            )
        except IntegrityError:
            return JsonResponse({"error": "Email already exists"}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred"}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)
