from django.db import models
from django.conf import settings


# articles/models.py
class Article(models.Model):
    # user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    # 현재 '활성화' 된 유저 모델에 대한 정보를 AUTH_USER_MODEL에 적기로 약속
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
