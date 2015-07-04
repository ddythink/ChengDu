from .models import Article, Rule, Project
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'url', 'publish_time')

class RulerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = ('name', 'allow_domains', 'enable')

# class InfotrackSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Infotrack
#         fields = ('id', 'add_num', 'sum_total', 'run_date','spend_time')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','pname', 'keywords', 'project_type', 'start_time','end_time','create_time','period', 'status',
                  'infotrack_ids')


