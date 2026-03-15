from django.db import models


class Dori(models.Model):
    nomi = models.CharField(max_length=200)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    ishlab_chiqaruvchi = models.CharField(max_length=200)
    ishlab_chiqarilgan_sana = models.DateField()
    amal_muddati = models.DateField()
    miqdor = models.IntegerField()
    kategoriya = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} | {self.nomi}"