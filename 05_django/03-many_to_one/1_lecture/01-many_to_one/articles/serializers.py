# articles/serializers.py

from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('created_at', 'updated_at',)


# 게시글 조회 할 때 해당 게시글의 댓글도 함께 조회
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)   # 댓글의 id와 content만 보여준다.

    # read_only=True 옵션을 통해 해당 필드를 읽기 전용으로 설정할 수 있다.
    comment_set = CommentDetailSerializer(many=True, read_only=True) # related_name을 통해 역참조
    # 댓글 갯수 표시
    num_of_comments = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = '__all__'
        # # fields = ('id', 'title',)
        # exclude = ('created_at', 'updated_at',)

    def get_num_of_comments(self, obj):
        # 여기서 obj는 Serializer가 처리하는 Article 인스턴스
        # view에서 annotate 한 필드를 그대로 사용 가능
        return obj.num_of_comments


# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    # article 필드 재정의 (id, title)
    class ArticleForCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id','title', )
            
    article = ArticleForCommentSerializer(read_only=True) 

    class Meta:
        model = Comment
        # 사용자에게 보여줄 데이터 또는 사용자가 보낼 데이터
        # 댓글을 `생성`할 때는 article의 정보를 `서버`가 처리
        # 댓글을 `조회`할 떄는 article의 정보도 포함해서 반환
        # fields = ('content', ) # tuple에 요소 1개일 때 ',' 찍기
        fields = '__all__'
        # read_only_fields = ('article', )