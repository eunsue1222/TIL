from rest_framework import serializers
from .models import Article

# 전체 목록만을 위한 시리얼라이저
class ArticleListSerializer(serializers.ModelSerializer):
    # 직렬화
    class Meta:
        # 모델에 대한 정보
        model = Article
        # fields = '__all__'
        fields = ('id', 'title')
    
# 범용적으로 게시글에 대한 전반적인 처리가 가능한 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'