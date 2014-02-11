from django.db import models

class question(models.Model):
    Q_text = models.CharField(max_length = 150,null=True, blank=True)
    response1 = models.CharField(max_length = 150,null=True, blank=True)
    response2 = models.CharField(max_length = 150,null=True, blank=True)
    response3 = models.CharField(max_length = 150,null=True, blank=True)
    response4 = models.CharField(max_length = 150,null=True, blank=True)
    response5 = models.CharField(max_length = 150,null=True, blank=True)
    def __unicode__(self):
        return self.Q_text

    class Meta:
        db_table = "primatequiz_question"


