from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_get_or_create(request):
    if request.method == 'GET':
        # 전체 게시글 조회
        articles = Article.objects.all()
        # serializer 정의. id, title만 보여주고 싶음.
        serializer = ArticleListSerializer(articles, many=True)
        # DRF로 인해 만들어진 직렬화. 직렬화를 마친 객체의 data만 사용자에게 반환. ERF 반환 방식으로 반환.
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        # 사용자가 보낸 데이터로 articles/를 생성하고, 정보가 유효한지 검증하고, 정상이면 저장하고, 반환한다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)