from rest_framework.decorators import api_view
from .models import Letter
from rest_framework.response import Response
from .serializers import LettersListSerializer
from .models import Letter

# Create your views here.
@api_view(['GET'])
def letters_list(request):
    letters = Letter.objects.all()
    serializer = LettersListSerializer(letters, many=True)
    return Response(serializer.data)