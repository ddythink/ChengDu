from django.contrib import admin

# Register your models here.
from .models import Ruler
from .models import Article, Project, Siteproperty, RelationAP, RelationAS

class RulerAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_urls','attr','enable']

class ArticleAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'publish_time', 'spider_from', 'crawler_time']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pname', 'keywords', 'thetype', 'status', 'final_time','create_time']

class SitepropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain', 'locate', 'nature', 'flag']

class RelationAPAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'article']

class RelationASAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'site_property']

admin.site.register(Ruler, RulerAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Siteproperty, SitepropertyAdmin)
admin.site.register(RelationAP, RelationAPAdmin)
admin.site.register(RelationAS, RelationASAdmin)

