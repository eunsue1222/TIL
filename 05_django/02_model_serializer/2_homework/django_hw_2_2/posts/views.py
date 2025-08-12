from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostListSerializer, PostSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def post_get_or_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)