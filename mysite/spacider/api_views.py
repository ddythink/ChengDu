from rest_framework import viewsets, status
from serializers import ArticleSerializer, RulerSerializer
from serializers import ProjectSerializer
from .models import Article, Rule, Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class RulerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RulerSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@api_view(['GET'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def infotrack_trend(request, project_id):
     try:
        project = Project.objects.get(pk=project_id)
        infotracks = Infotrack.objects.filter(project=project)
        if infotracks:
            serializer = InfotrackSerializer(infotracks, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
     except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
