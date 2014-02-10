from django.db import models
from PIL import Image
from base.settings import MEDIA_ROOT
import os
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        return self.sciname

# ##attempt to resize images for mobile
#     def save(self):
#         super(species, self).save()
#         try:
#             infile = os.path.join(MEDIA_ROOT, str(self.pic.name))
#             outfile = infile.replace(".jpg", "-MOBILE.jpg")
#             im = Image.open(infile)
#             img_ratio = im.size[0] / float(im.size[1])
#             thumb = im.thumbnail(700,700*img_ratio, Image.ANTIALIAS)
#
#             thumb_io = StringIO.StringIO()
#             thumb.save(thumb, format='JPEG')
#
# # Create a new Django file-like object to be used in models as ImageField using
# # InMemoryUploadedFile.  If you look at the source in Django, a
# # SimpleUploadedFile is essentially instantiated similarly to what is shown here
#             thumb_file = InMemoryUploadedFile(thumb_io, None, outfile, 'image/jpeg',
#                                   thumb_io.len, None)
#             self.picmobile = thumb_file
#         except:
#             print "cannot create thumbnail"
#
#         super(species, self).save()

class question(models.Model):
    Q_text = models.CharField(max_length = 150,null=True, blank=True)
    response1 = models.CharField(max_length = 150,null=True, blank=True)
    response2 = models.CharField(max_length = 150,null=True, blank=True)
    response3 = models.CharField(max_length = 150,null=True, blank=True)
    response4 = models.CharField(max_length = 150,null=True, blank=True)
    response5 = models.CharField(max_length = 150,null=True, blank=True)
    def __unicode__(self):
        return self.Q_text



