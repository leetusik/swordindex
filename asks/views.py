from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from .models import Ask


@require_POST
def submit_form(request):
    """Handle contact form submissions"""
    try:
        # Extract form data
        company = request.POST.get("comp", "")
        name = request.POST.get("name")
        email = request.POST.get("mail")
        content = request.POST.get("cont")

        # Validate required fields (company is now optional)
        if not all([name, email, content]):
            return HttpResponse(
                '<div class="mt-4 p-4 bg-red-900/30 border border-red-500 rounded-lg text-center">'
                "이름, 이메일, 문의내용은 필수 입력사항입니다."
                "</div>",
                status=400,
            )

        # Save to database (company can be empty)
        Ask.objects.create(
            company=company if company else None,
            name=name,
            email=email,
            content=content,
        )

        # Return success message with JavaScript to clear the form
        return HttpResponse(
            '<div class="mt-4 p-4 bg-primary/10 border border-primary rounded-lg text-center">'
            "문의가 성공적으로 제출되었습니다. 곧 연락드리겠습니다."
            "</div>"
            "<script>"
            'document.getElementById("comp").value = "";'
            'document.getElementById("name").value = "";'
            'document.getElementById("mail").value = "";'
            'document.getElementById("cont").value = "";'
            "</script>"
        )

    except Exception as e:
        # Log the error (in a real app, you'd use proper logging)
        print(f"Error in submit_form: {e}")

        # Return error message
        return HttpResponse(
            '<div class="mt-4 p-4 bg-red-900/30 border border-red-500 rounded-lg text-center">'
            "문의 제출 중 오류가 발생했습니다. 나중에 다시 시도해주세요."
            "</div>",
            status=500,
        )
