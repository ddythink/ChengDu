from django.contrib import admin

# Register your models here.
from .models import Ruler
from .models import Article, Project, Siteproperty, RelationAP, RelationAS

class RulerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_urls','enable']

class ArticleAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'publish_time', 'spider_from', 'crawler_time']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'keywords', 'thetype', 'status', 'final_time']

admin.site.register(Ruler, RulerAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Siteproperty)
#admin.site.register(RelationAP)
#admin.site.register(RelationAS) do not showing up to the admin

