from rest_framework import viewsets, status
from serializers import ArticleSerializer, RulerSerializer
from serializers import InfotrackSerializer,ProjectSerializer
from .models import Article, Ruler,Infotrack,Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class RulerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ruler.objects.all()
    serializer_class = RulerSerializer

class InfotrackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Infotrack.objects.all()
    serializer_class = InfotrackSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class InfotrackDetail(APIView):
    def get_object(self, pk):
        try:
            return Infotrack.objects.get(pk=pk)
        except Infotrack.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        infotrack = self.get_object(pk)
        serializer = InfotrackSerializer(infotrack)
        return Response(serializer.data)



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

