from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from turbotailer.autoarticles.api.serializers import ArticleSerializer, ArticleTopicSerializer
from turbotailer.autoarticles.models import ArticleTopic


@api_view(["POST"])
def article_create_view(request):
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def topic_create_view(request):
    """
    Create an ArticleTopic instance.
    """
    if request.method == "POST":
        serializer = ArticleTopicSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def topic_list_view(request):
    """
    List all topics.
    """
    if request.method == "GET":
        topics = ArticleTopic.objects.filter(has_article=False, is_ready=True)
        serializer = ArticleTopicSerializer(topics, many=True)
        return Response(serializer.data)


@api_view(["PATCH"])
def topic_update_view(request, topic_id):
    """
    Update topic
    """
    if request.method == "PATCH":
        # Get the topic instance
        topic = get_object_or_404(ArticleTopic, pk=topic_id)

        topic.has_article = True
        topic.save()
        return Response({"message": "Topic updated"})
