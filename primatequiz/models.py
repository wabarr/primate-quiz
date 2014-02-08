from django.db import models

# Create your models here.
class species(models.Model):
    sciname = models.CharField(max_length = 200,null=True, blank=True)
    slug = models.SlugField(unique=True)
    commonname = models.CharField(max_length = 200,null=True, blank=True)
    description = models.TextField(max_length = 600, null=True, blank=True)
    funfact = models.CharField(max_length = 200,null=True, blank=True)
    pic = models.ImageField(upload_to="pics/%Y/%m/%d")

    class Meta:
        verbose_name_plural = "species"

    def __unicode__(self):
        return self.sciname

class question(models.Model):
    Q_text = models.CharField(max_length = 150,null=True, blank=True)
    response1 = models.CharField(max_length = 150,null=True, blank=True)
    response2 = models.CharField(max_length = 150,null=True, blank=True)
    response3 = models.CharField(max_length = 150,null=True, blank=True)
    response4 = models.CharField(max_length = 150,null=True, blank=True)
    response5 = models.CharField(max_length = 150,null=True, blank=True)
    def __unicode__(self):
        return self.Q_text



