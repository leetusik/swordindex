from django.db import models
from django.utils import timezone


class Ask(models.Model):
    company = models.CharField(
        max_length=255, verbose_name="소속", blank=True, null=True
    )
    name = models.CharField(max_length=100, verbose_name="이름")
    email = models.EmailField(verbose_name="이메일")
    content = models.TextField(verbose_name="문의내용")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="등록일")
    is_processed = models.BooleanField(default=False, verbose_name="처리여부")

    class Meta:
        verbose_name = "문의"
        verbose_name_plural = "문의"
        ordering = ["-created_at"]

    def __str__(self):
        company_str = self.company if self.company else "미지정"
        return f"{self.name} - {company_str} ({self.created_at.strftime('%Y-%m-%d')})"
