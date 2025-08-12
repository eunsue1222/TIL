from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .serializers import PostListSerializer, PostSerializer

@api_view(['GET', 'POST'])
def post_get_or_create(request):    
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request, post_pk):
    posts = Post.objects.get(pk=post_pk)

    if request.method == 'GET':
        # posts = Post.objects.all()
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    if request.method == 'DELETE':
        posts.delete()
        return Response(
            {'message': 'Post deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
    
    elif request.method == 'PUT':
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
# @api_view(['GET', 'POST', 'DELETE', 'PUT'])
# def post_handler(request, post_pk):
#     posts = Post.objects.get(pk=post_pk)

#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostListSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PostListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         posts.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'PUT':
#         serializer = PostListSerializer(posts, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
