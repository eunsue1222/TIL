from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = Article.objects.annotate(num_of_comments=Count('comment')).get(
        pk=article_pk
    )
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk) # 게시글 지정
    serealizer = CommentSerializer(data=request.data) # 사용자가 보낸 댓글 정보 저장
    if serealizer.is_valid(raise_exception=True): # 유효성 검사
        serealizer.save(article=article) # article 정보 DB에 반영
        return Response(serealizer.data, status=status.HTTP_201_CREATED) # 댓글 정보 사용자에게 반환


# 모든 댓글 조회
@api_view(['GET'])
def comment_list(request):
   pass

# 댓글 pk 값으로 조회, 삭제, 수정
@api_view(['GET'])
def comment_detail(request, comment_pk):
    pass
   

