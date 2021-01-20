from __future__ import unicode_literals

from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    text_content = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='news', null=True)
    reference_date = models.DateField()
    publish_date = models.DateField()
    blog_page = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
