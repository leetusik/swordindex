from django.contrib import admin

from .models import Ask


@admin.register(Ask)
class AskAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "created_at", "is_processed")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "company", "email", "content")
    date_hierarchy = "created_at"
    list_per_page = 20

    fieldsets = (
        ("기본 정보", {"fields": ("company", "name", "email")}),
        ("문의 내용", {"fields": ("content",)}),
        ("관리 정보", {"fields": ("created_at", "is_processed")}),
    )

    readonly_fields = ("created_at",)
