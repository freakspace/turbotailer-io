from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from turbotailer.autoarticles.api.serializers import ArticleSerializer


@api_view(["POST"])
def article_create_view(request):
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
