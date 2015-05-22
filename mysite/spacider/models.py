from django.db import models

# Create your models here.

class Ruler(models.Model):

    name = models.CharField(max_length=50)
    allow_domains = models.CharField(max_length=256)
    start_urls = models.CharField(max_length=256)
    next_page = models.CharField(max_length=256)
    allow_url =  models.CharField(max_length=256)
    extract_from =  models.CharField(max_length=256)
    title_xpath =  models.CharField(max_length=256)
    body_xpath =  models.CharField(max_length=256)
    publish_time_xpath =  models.CharField(max_length=256)
    source_site_xpath =  models.CharField(max_length=256)
    enable = models.IntegerField(default=0)
    #create_at = models.DateTimeField()
    #update_at = models.DateTimeField()

    def __unicode__(self):
        return self.name + " "+self.allow_domains








