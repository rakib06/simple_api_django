from django.db import models

# Create your models here.


class Hadith(models.Model):

    parent = models.ForeignKey('self', null=True, related_name='children', on_delete='SET_NULL', blank=True)
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)
    description_arb = models.TextField(null=True, blank=True)
    description_bn = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
