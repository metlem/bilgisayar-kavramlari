from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yazar = models.ForeignKey('auth.User')   
    y_tarihi = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=300, blank=True, null=True)



    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik