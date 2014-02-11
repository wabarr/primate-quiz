from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class species(models.Model):
    sciname = models.CharField(max_length = 200,null=True, blank=True)
    slug = models.SlugField(unique=True)
    commonname = models.CharField(max_length = 200,null=True, blank=True)
    description = models.TextField(max_length = 600, null=True, blank=True)
    funfact = models.CharField(max_length = 200,null=True, blank=True)
    pic = models.ImageField(upload_to="pics/%Y/%m/%d",help_text="between 1000 - 1300px width")
    picmobile = models.ImageField(upload_to="pics/%Y/%m/%d", help_text="between 400 - 600px width")
    class Meta:
        verbose_name_plural = "species"

    def __unicode__(self):
        return self.commonname + " (" + self.sciname + ")"

    def get_absolute_url(self):
        return reverse('primatequiz.views.results', args=[self.slug])