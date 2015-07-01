from django.contrib import admin

# Register your models here.
from .models import Rule, Article, Project, Siteproperty

class RuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_urls','attr','enable']

class ArticleAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'publish_time', 'spider_from', 'crawler_time']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pname', 'keywords', 'project_type', 'status', 'period','create_time']

class SitepropertyAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'domain', 'locate', 'nature', 'flag']

# class InfotrackAdmin(admin.ModelAdmin):
#      list_display = ['id', 'project', 'run_date', 'add_num', 'sum','spider_from']

admin.site.register(Rule, RuleAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Siteproperty, SitepropertyAdmin)

