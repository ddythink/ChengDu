from rest_framework import viewsets, status
from serializers import ArticleSerializer, RulerSerializer, InfotrackSerializer,ProjectSerializer
from .models import Article, Ruler,Infotrack,Project
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class RulerViewSet(viewsets.ModelViewSet):
    queryset = Ruler.objects.all()
    serializer_class = RulerSerializer

class InfotrackViewSet(viewsets.ModelViewSet):
    queryset = Infotrack.objects.all()
    serializer_class = InfotrackSerializer

class ProjectViewSet(viewsets.ModelViewSet):
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

