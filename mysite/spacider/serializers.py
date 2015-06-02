from .models import Article, Ruler, Infotrack, Project
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'url', 'publish_time')

class RulerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruler
        fields = ('name', 'allow_domains', 'enable')

class InfotrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Infotrack
        fields = ('add_num', 'sum_total', 'run_date')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','pname', 'keywords', 'thetype', 'start_time','end_time','final_time', 'status', 'create_time')
