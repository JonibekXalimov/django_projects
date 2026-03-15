from django.db import models


class Mijoz(models.Model):
    ismi = models.CharField(max_length=20)
    nomer = models.CharField(max_length=20)
    manzil = models.CharField(max_length=17)
    yoshi = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}     | {self.ismi}"
     