from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 인증과 관련된 테이블 설정 시, 장고는 User 모델의 기본 제공 필드들까지도 custom해서 등록하기를 강력히 권장
    # 기존 django가 제공해주는 인증, 권한, auth 모델과의 연관 관계가 모두 수정되지 않으므로 settings.py 설정
    pass
