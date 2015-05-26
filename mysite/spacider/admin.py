from django.contrib import admin

# Register your models here.
from .models import Ruler
from .models import Article, Project, Siteproperty, RelationAP, RelationAS

admin.site.register(Ruler)
admin.site.register(Article)
admin.site.register(Project)
admin.site.register(Siteproperty)
admin.site.register(RelationAP)
admin.site.register(RelationAS)

