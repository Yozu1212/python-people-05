from django.db import models

class peopledata(models.Model):
    statistic_yyymm = models.CharField(max_length=100)
    svillage = models.IntegerField(default=0)
    household_no = models.IntegerField(default=0)
    people_total = models.IntegerField(default=0)
    birth_total = models.IntegerField(default=0)
    death_m = models.IntegerField(default=0)
    death_f = models.IntegerField(default=0)
    def __str__(self):
        return self.svillage

class NKUSTnews(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class PhoneMaker(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    maker = models.ForeignKey(PhoneMaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-price"]

class StockInfo(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    mprice = models.FloatField()

    def __str__(self):
        return self.name 